# 美容院のルールを実装する(予約できるか判定，空き時間確認など)
from backend.models.reservation import Reservation
from backend.repositories.reservation_repository import ReservationRepository
from backend.utils.time_utils import generate_times

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
        """ユーザーの予約一覧を取得"""

        reservations = self.repository.load_all()

        return [
            reservation
            for reservation in reservations
            if reservation.user_id == user_id
        ]

    def get_daily_schedule(self, date, stylist_id):
        """予約可能時間確認"""
        reservations = self.repository.load_all()

        reserved_times = set()

        for r in reservations:
            if r.date == date and r.stylist_id == stylist_id:
                reserved_times.add(r.time)

        all_times = generate_times()

        schedule = {}

        for time in all_times:

            if time in reserved_times:
                schedule[time] = "×"

            else:
                schedule[time] = "○"

        return schedule