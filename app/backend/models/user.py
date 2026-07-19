from dataclasses import dataclass

@dataclass
class User:
    """会員情報"""

    user_id: int                 # 会員ID
    name: str               # 名前
    email: str              # メールアドレス
    phone: str              # 電話番号
    password: str           # パスワード
    role: str = "customer"  