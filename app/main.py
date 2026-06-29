from backend.services.reservation_service import ReservationService

def main():
    service = ReservationService()

    print("予約システム起動")

    # テスト用（あとで消す）
    print(service.get_reservations())

if __name__ == "__main__":
    main()