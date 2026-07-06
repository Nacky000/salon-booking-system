from backend.services.menu_service import MenuService
from backend.services.user_service import UserService
from backend.services.stylist_service import StylistService


class AdminService:
    """
    管理画面で利用するサービス

    ReservationService は他担当が実装するため、
    現時点ではメニュー・会員・美容師の管理のみ担当する。
    """

    def __init__(self):
        self.menu_service = MenuService()
        self.user_service = UserService()
        self.stylist_service = StylistService()

    # --------------------
    # ダッシュボード
    # --------------------

    def get_dashboard_data(self):
        """
        ダッシュボード表示用データ
        """

        users = self.user_service.get_all_users()
        menus = self.menu_service.get_all()
        stylists = self.stylist_service.get_all()

        return {
            "user_count": len(users),
            "menu_count": len(menus),
            "stylist_count": len(stylists)
        }

    # --------------------
    # 会員
    # --------------------

    def get_all_users(self):
        return self.user_service.get_all_users()

    def get_user(self, user_id):
        return self.user_service.get_user_by_id(user_id)

    # --------------------
    # メニュー
    # --------------------

    def get_all_menus(self):
        return self.menu_service.get_all()

    def add_menu(self, name, price, duration):
        return self.menu_service.add_menu(
            name,
            price,
            duration
        )

    def update_menu(self, menu_id, name, price, duration):
        return self.menu_service.update_menu(
            menu_id,
            name,
            price,
            duration
        )

    def delete_menu(self, menu_id):
        self.menu_service.delete_menu(menu_id)

    # --------------------
    # 美容師
    # --------------------

    def get_all_stylists(self):
        return self.stylist_service.get_all()

    def add_stylist(self, name):
        return self.stylist_service.add_stylist(name)

    def update_stylist(self, stylist_id, name, holiday):
        return self.stylist_service.update_stylist(
            stylist_id,
            name,
            holiday
        )

    def delete_stylist(self, stylist_id):
        self.stylist_service.delete_stylist(stylist_id)
# 管理画面は各Serviceを直接触らず、AdminServiceだけを呼び出せばよいという設計になります。