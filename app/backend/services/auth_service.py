from backend.repositories.user_repository import UserRepository


class AuthService:

    def __init__(self):
        self.repository = UserRepository()

    def login(self, email, password):
        """
        ログイン認証
        """

        user = self.repository.find_by_email(email)

        if user is None:
            return None

        if user.password != password:
            return None

        return user

    def is_admin(self, user):
        """
        管理者か判定
        """

        if user is None:
            return False

        return user.role == "admin"
    

# ログインの流れ
# メール入力
#       ↓
# ユーザー検索
#       ↓
# パスワード一致？
#       ↓
# 成功ならUser
# 失敗ならNone
# 
# パスワードは平文で保存しているため、実運用ではハッシュ化が必要。(今は実習の場であるから今回は省略)