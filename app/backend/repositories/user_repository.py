import json
import os

from backend.models.user import User


class UserRepository:

    def __init__(self):
        self.file_path = os.path.join(
            os.path.dirname(__file__),
            "../../data/users.json"
        )

    def load_users(self):
        """全ユーザー情報を取得"""
        
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [User(**user) for user in data]

    def save_users(self, users):
        """ユーザー一覧を保存"""
        data = [user.__dict__ for user in users]

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def find_by_email(self, email):
        """メールアドレス検索"""
        users = self.load_users()

        for user in users:
            if user.email == email:
                return user

        return None

    def find_by_id(self, user_id):
        """ユーザー検索"""
        users = self.load_users()

        for user in users:
            if user.user_id == user_id:
                return user

        return None

    def add_user(self, user):
        """ユーザー追加"""
        users = self.load_users()
        users.append(user)

        self.save_users(users)

# このフィイルでは

# users.json
#       ↑
# 読み込み
#       ↓
# Userオブジェクトへ変換

# 逆に

# Userオブジェクト
#       ↓
# 辞書へ変換
#       ↓
# users.jsonへ保存

# を行う。