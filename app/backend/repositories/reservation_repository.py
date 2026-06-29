import json
from pathlib import Path
from dataclasses import asdict

from backend.models.reservation import Reservation

# reservations.jsonへのパス
DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "reservations.json" # 実行場所が変わっても動くように指定

class ReservationRepository:

    def load_all(self):
        """予約一覧を取得"""
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f) # ファイルを開いて読み込みモードでJSONを開く

        reservations = []

        for item in data:
            reservations.append(Reservation(**item)) # Reservationに変換しリストに追加

        return reservations

    def save_all(self, reservations):
        """予約一覧を保存"""
        data = []

        for reservation in reservations:
            data.append(asdict(reservation)) # JSONとして保存できる辞書を入れる

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4) # JSONへ保存する

    def add(self, reservation):
        """予約を追加"""
        reservations = self.load_all() # 予約一覧を取得
        reservations.append(reservation) # 新しい予約を追加
        self.save_all(reservations) # 保存

    def find_by_id(self, reservation_id):
        """IDで予約を検索"""
        reservations = self.load_all() # 全予約を取得

        for reservation in reservations: # 1件ずつ見ていく
            if reservation.id == reservation_id: # IDが一致するものが見つかったら返す
                return reservation

        return None # 見つからなければNoneを返す

    def delete(self, reservation_id):
        """予約を削除"""
        reservations = self.load_all() # 予約一覧を取得

        new_reservations = [] # 削除しない予約を入れる用のリスト

        for reservation in reservations:
            if reservation.id != reservation_id: # 1件ずつ見て削除しないものだけ残す
                new_reservations.append(reservation)

        self.save_all(new_reservations) # 削除しない予約リストを保存する