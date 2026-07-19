import json
import os

from backend.models.stylist import Stylist


class StylistRepository:

    def __init__(self):
        self.file_path = os.path.join(
            os.path.dirname(__file__),
            "../../data/stylists.json"
        )

    def load_stylists(self):
        """全スタイリストを取得"""

        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [Stylist(**stylist) for stylist in data]

    def save_stylists(self, stylists):
        """スタイリスト一覧を保存"""

        data = [stylist.__dict__ for stylist in stylists]

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def find_by_id(self, stylist_id):
        """スタイリストのID検索"""

        stylists = self.load_stylists()

        for stylist in stylists:
            if stylist.stylist_id == stylist_id:
                return stylist

        return None

    def add_stylist(self, stylist):
        """スタイリスト追加"""

        stylists = self.load_stylists()

        stylists.append(stylist)

        self.save_stylists(stylists)

    def delete_stylist(self, stylist_id):
        """スタイリスト削除"""

        stylists = self.load_stylists()

        stylists = [s for s in stylists if s.stylist_id != stylist_id]

        self.save_stylists(stylists)

# このフィイルでは

# stylists.json
#       ↑
# 読み込み
#       ↓
# Stylistオブジェクトへ変換

# 逆に

# Stylistオブジェクト
#       ↓
# 辞書へ変換
#       ↓
# stylists.jsonへ保存
#
# を行う。

# 