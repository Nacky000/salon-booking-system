from backend.models.menu import Menu
from backend.repositories.menu_repository import MenuRepository


class MenuService:

    def __init__(self):
        self.repository = MenuRepository()

    def get_all(self):
        """
        全メニュー取得
        """
        return self.repository.load_menus()

    def get_by_id(self, menu_id):
        """
        IDからメニュー取得
        """
        return self.repository.find_by_id(menu_id)

    def add_menu(self, name, price, duration):
        """
        メニュー追加
        """

        menus = self.repository.load_menus()

        if menus:
            new_id = max(menu.menu_id for menu in menus) + 1
        else:
            new_id = 1

        menu = Menu(
            menu_id=new_id,
            name=name,
            price=price,
            duration=duration
        )

        self.repository.add_menu(menu)

        return menu

    def update_menu(self, menu_id, name, price, duration):
        """
        メニュー更新
        """

        menus = self.repository.load_menus()

        for menu in menus:
            if menu.menu_id == menu_id:
                menu.name = name
                menu.price = price
                menu.duration = duration

                self.repository.save_menus(menus)

                return menu

        return None

    def delete_menu(self, menu_id):
        """
        メニュー削除
        """
        self.repository.delete_menu(menu_id)


# 現在の一覧取得
#       ↓
# 最大ID取得
#       ↓
# +1
#       ↓
# Menu作成
#       ↓
# Repositoryへ保存

# 更新の際は、
# 一覧取得
#       ↓
# 対象ID検索
#       ↓
# 値変更
#       ↓
# save_menus()