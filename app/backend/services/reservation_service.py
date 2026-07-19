# 美容院のルールを実装する(予約できるか判定，空き時間確認など)
from backend.models.reservation import Reservation
from backend.repositories.reservation_repository import ReservationRepository
from backend.utils.time_utils import generate_times
from backend.services.menu_service import MenuService
from backend.services.stylist_service import StylistService
from datetime import datetime, timedelta

class ReservationService:

    def __init__(self):
        self.repository = ReservationRepository() # Repositoryを使えるように準備する

    def create_reservation(
        self,
        user_id,
        menu_ids,
        stylist_id,
        date,
        time
    ):
        """予約登録"""
        
        if time not in generate_times():
            return "invalid_time"
    

        # 施術時間チェック
        menu_service = MenuService()
        total_duration = 0

        for menu_id in menu_ids:
            menu = menu_service.get_by_id(menu_id)

            if menu:
                total_duration += menu.duration

        start_time = datetime.strptime(
            time,
            "%H:%M"
        )

        end_time = (
            start_time
            + timedelta(minutes=total_duration)
        )

        closing_time = datetime.strptime(
            "18:00",
            "%H:%M"
        )

        if end_time > closing_time:
            return "outside_business_hours"
        
        reservations = self.repository.load_all() # 現在の予約一覧を取得

        for reservation in reservations: # 同じ美容師・同じ日付・同じ時間に予約がないか確認
            if (
                reservation.date == date
                and reservation.time == time
                and reservation.stylist_id == stylist_id
            ):
                return "duplicate"  # 予約できない

        if reservations: # 新しい予約IDを決定
            new_id = max(reservation.id for reservation in reservations) + 1
        else:
            new_id = 1

        reservation = Reservation( # 新しい予約を作成
            id=new_id,
            user_id=user_id,
            menu_ids=menu_ids,
            stylist_id=stylist_id,
            date=date,
            time=time
        )

        self.repository.add(reservation) # 保存

        return "success"

    def cancel_reservation(self, reservation_id):
        """予約キャンセル"""
        reservations = self.repository.load_all()

        for reservation in reservations:
            if reservation.id == reservation_id:
                reservation.status = "cancelled"
                self.repository.save_all(reservations)
                return True

        return False

    def get_reservations(self):
        """予約一覧取得"""
        return self.repository.load_all()
    
    def get_user_reservations(self, user_id):
        """ユーザーの予約一覧（予約中のみ）"""

        reservations = [
            reservation
            for reservation in self.repository.load_all()
            if reservation.user_id == user_id
            and reservation.status == "reserved"
        ]

        menu_service = MenuService()
        stylist_service = StylistService()

        for reservation in reservations:

            # 美容師名
            stylist = stylist_service.get_by_id(reservation.stylist_id)
            reservation.stylist_name = stylist.name if stylist else "不明"

            # メニュー名
            menu_names = []

            for menu_id in reservation.menu_ids:
                menu = menu_service.get_by_id(menu_id)

                if menu:
                    menu_names.append(menu.name)

            reservation.menu_names = menu_names

            # 日本語ステータス
            reservation.status_text = "予約中"

        return reservations

    def get_daily_schedule(
        self,
        date,
        stylist_id,
        menu_ids
    ):
        """予約可能時間確認"""

        reservations = self.repository.load_all()
        reserved_times = set()
        menu_service = MenuService()

        for r in reservations:
            if r.date == date and r.stylist_id == stylist_id:
                total_duration = 0
                # メニュー時間合計
                for menu_id in r.menu_ids:
                    menu = menu_service.get_by_id(menu_id)

                    if menu:
                        total_duration += menu.duration

                # 開始時間から30分ごとに埋める
                start = datetime.strptime(
                    r.time,
                    "%H:%M"
                )

                for i in range(total_duration // 30):
                    t = (
                        start + timedelta(minutes=30*i)
                    ).strftime("%H:%M")

                    reserved_times.add(t)

        # 全時間作成
        all_times = generate_times()
        menu_service = MenuService()
        duration = 0

        for menu_id in menu_ids:
            menu = menu_service.get_by_id(menu_id)

            if menu:
                duration += menu.duration

        schedule = {}

        for time in all_times:
            start = datetime.strptime(
                time,
                "%H:%M"
            )

            end = start + timedelta(
                minutes=duration
            )

            closing = datetime.strptime(
                "18:00",
                "%H:%M"
            )

            if end > closing:
                schedule[time] = "×"
                continue

            if time in reserved_times:
                schedule[time] = "×"
            else:
                schedule[time] = "○"


        return schedule