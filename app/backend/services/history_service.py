from backend.repositories.reservation_repository import ReservationRepository


class HistoryService:
    """
    予約履歴取得サービス
    """

    def __init__(self):
        self.repository = ReservationRepository()

    def get_history(self, user_id):
        """
        指定ユーザーの予約履歴を取得
        """

        reservations = self.repository.get_all()

        histories = [
            reservation
            for reservation in reservations
            if reservation.user_id == user_id
        ]

        return histories