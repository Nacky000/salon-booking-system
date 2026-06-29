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
                return False  # 予約できない

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

        return True

    def cancel_reservation(self, reservation_id):
        """予約キャンセル"""
        reservation = self.repository.find_by_id(reservation_id) # ID検索する

        if reservation is None: # 見つからない場合
            return False

        self.repository.delete(reservation_id) # 見つかった場合，削除する
        return True

    def get_reservations(self):
        """予約一覧取得"""
        return self.repository.load_all()

    def get_available_times(self, date, stylist_id):
        """空き時間取得"""

        reservations = self.repository.load_all() # 現在の予約一覧を取得
        reserved_times = set() # 予約済みの時間を取得

        for reservation in reservations:
            if (
                reservation.date == date
                and reservation.stylist_id == stylist_id
            ):
                reserved_times.add(reservation.time)
                
        all_times = generate_times() # 予約時間

        available_times = [] # 空いている時間だけ返す

        for time in all_times:
            if time not in reserved_times:
                available_times.append(time)

        return available_times