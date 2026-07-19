import json
import os

from backend.models.menu import Menu


class MenuRepository:

    def __init__(self):
        self.file_path = os.path.join(
            os.path.dirname(__file__),
            "../../data/menus.json"
        )

    def load_menus(self):
        """全メニューを取得"""

        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [Menu(**menu) for menu in data]

    def save_menus(self, menus):
        """メニュー一覧を保存"""

        data = [menu.__dict__ for menu in menus]

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def find_by_id(self, menu_id):
        """ID検索"""

        menus = self.load_menus()

        for menu in menus:
            if menu.menu_id == menu_id:
                return menu

        return None

    def add_menu(self, menu):
        """メニュー追加"""

        menus = self.load_menus()
        menus.append(menu)
        self.save_menus(menus)

    def delete_menu(self, menu_id):
        """メニュー削除"""

        menus = self.load_menus()

        menus = [m for m in menus if m.id != menu_id]

        self.save_menus(menus)

# このフィイルでは

# menus.json
#       ↑
# 読み込み
#       ↓
# Menuオブジェクトへ変換

# 逆に

# Menuオブジェクト
#       ↓
# 辞書へ変換
#       ↓
# menus.jsonへ保存

# を行う。



# 例えば、以下のコードでデータの操作が可能。

# repo = MenuRepository()

# menus = repo.load_menus()

# menu = repo.find_by_id(1)

# repo.add_menu(Menu(3, "パーマ", 8000, 120))