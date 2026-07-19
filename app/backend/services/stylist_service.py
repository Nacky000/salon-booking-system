from backend.models.stylist import Stylist
from backend.repositories.stylist_repository import StylistRepository


class StylistService:

    def __init__(self):
        self.repository = StylistRepository()

    def get_all(self):
        """
        全美容師取得
        """
        return self.repository.load_stylists()

    def get_by_id(self, stylist_id):
        """
        IDから美容師取得
        """
        return self.repository.find_by_id(stylist_id)

    def add_stylist(self, name):
        """
        美容師追加
        """

        stylists = self.repository.load_stylists()

        if stylists:
            new_id = max(stylist.stylist_id for stylist in stylists) + 1
        else:
            new_id = 1

        stylist = Stylist(
            id=new_id,
            name=name,
            holiday=[]
        )

        self.repository.add_stylist(stylist)

        return stylist

    def update_stylist(self, stylist_id, name, holiday):
        """
        美容師情報更新
        """

        stylists = self.repository.load_stylists()

        for stylist in stylists:
            if stylist.stylist_id == stylist_id:
                stylist.name = name
                stylist.holiday = holiday

                self.repository.save_stylists(stylists)

                return stylist

        return None

    def delete_stylist(self, stylist_id):
        """
        美容師削除
        """
        self.repository.delete_stylist(stylist_id)

    def is_holiday(self, stylist_id, date):
        """
        指定日に美容師が休みか判定
        """

        stylist = self.repository.find_by_id(stylist_id)

        if stylist is None:
            return False

        return date in stylist.holiday