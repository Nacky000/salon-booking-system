from dataclasses import dataclass

@dataclass
class Menu:
    """施術メニュー情報"""

    id: int         # メニューID
    name: str       # メニュー名
    price: int      # 料金
    duration: int   # 施術時間（分）