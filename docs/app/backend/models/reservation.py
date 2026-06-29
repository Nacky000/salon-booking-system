from dataclasses import dataclass

@dataclass
class Reservation:
    id: int
    user_id: int
    menu_ids: list[int]
    stylist_id: int
    date: str
    time: str
    status: str = "reserved"