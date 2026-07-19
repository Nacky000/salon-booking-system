from dataclasses import dataclass, field

@dataclass
class Stylist:
    """美容師情報"""

    stylist_id: int
    name: str
    holiday: list[str] = field(default_factory=list)


# holidayは

# holiday = [
#     "2026-07-15",
#     "2026-07-21"
# ]
# のように休日を保存する。

# 予約登録時には、

# holidayに予約日が入っているかを

# 確認することで判定可能