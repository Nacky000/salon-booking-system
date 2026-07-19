from backend.models.user import User
from backend.repositories.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def register_user(self, name, email, phone, password):
        """
        新規ユーザー登録
        """

        # メールアドレス重複確認
        if self.repository.find_by_email(email):
            raise ValueError("このメールアドレスは既に登録されています。")

        users = self.repository.load_users()

        # 新しいIDを採番
        if users:
            new_id = max(user.user_id for user in users) + 1
        else:
            new_id = 1

        new_user = User(
            user_id=new_id,
            name=name,
            email=email,
            phone=phone,
            password=password,
            role="customer"
        )

        self.repository.add_user(new_user)

        return new_user

    def get_user_by_id(self, user_id):
        """
        IDからユーザー取得
        """
        return self.repository.find_by_id(user_id)

    def get_user_by_email(self, email):
        """
        メールアドレスからユーザー取得
        """
        return self.repository.find_by_email(email)

    def get_all_users(self):
        """
        全ユーザー取得
        """
        return self.repository.load_users()
    

# このクラスでは
# service = UserService()
# 
# service.register_user(
#     "山田太郎",
#     "yamada@test.com",
#     "09011112222",
#     "password"
# )
# 
# とすると、
# メール重複確認
#         ↓
# ID決定
#         ↓
# User生成
#         ↓
# Repositoryへ保存
# までやってくれる。