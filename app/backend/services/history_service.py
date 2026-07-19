from backend.repositories.reservation_repository import ReservationRepository
from backend.services.menu_service import MenuService
from backend.services.stylist_service import StylistService


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

        reservations = [
            reservation
            for reservation in self.repository.load_all()
            if reservation.user_id == user_id
        ]

        menu_service = MenuService()
        stylist_service = StylistService()

        for reservation in reservations:

            # --------------------
            # 美容師名
            # --------------------
            stylist = stylist_service.get_by_id(reservation.stylist_id)

            if stylist:
                reservation.stylist_name = stylist.name
            else:
                reservation.stylist_name = "不明"

            # --------------------
            # メニュー名
            # --------------------
            menu_names = []

            for menu_id in reservation.menu_ids:

                menu = menu_service.get_by_id(menu_id)

                if menu:
                    menu_names.append(menu.name)

            reservation.menu_names = menu_names

            # --------------------
            # ステータス表示
            # --------------------
            if reservation.status == "reserved":
                reservation.status_text = "予約中"

            elif reservation.status == "cancelled":
                reservation.status_text = "キャンセル済み"

            elif reservation.status == "completed":
                reservation.status_text = "施術完了"

            else:
                reservation.status_text = reservation.status

        return reservations