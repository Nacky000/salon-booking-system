from backend.services.reservation_service import ReservationService
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend"
) # Flaskアプリ作成，設定

app.secret_key = "salon-booking-system" # 実用ではランダムな長い文字列とする


# --------------------
# トップページ
# --------------------
@app.route("/") 
def home():
    return render_template("home.html")

# --------------------
# 予約画面
# --------------------
@app.route("/reservation")
def reservation():

    # menu_service = MenuService()
    # stylist_service = StylistService()

    # menus = menu_service.get_all()
    # stylists = stylist_service.get_all()

    # return render_template(
    #     "reservation.html",
    #     menus=menus,
    #     stylists=stylists
    # )
    return render_template("reservation.html") # TODO: MenuService, StylistServiceから一覧を取得して渡す

# --------------------
# 予約一覧
# --------------------
@app.route("/reservation/list")
def reservation_list():

    if "user_id" not in session:
        return redirect(url_for("login"))
    
    service = ReservationService()

    reservations = service.get_user_reservations(
        session["user_id"]
    )

    return render_template(
        "reservation_list.html",
        reservations=reservations
    )

# --------------------
# 予約登録
# --------------------
@app.route("/reservation/create", methods=["POST"])
def create_reservation():

    service = ReservationService() # 予約サービスを利用

    # フォームから入力内容を取得
    user_id = int(request.form["user_id"]) # TODO: 会員機能実装後は session["user_id"] を使用
    menu_ids = [int(menu_id) for menu_id in request.form.getlist("menu_ids")]
    stylist_id = int(request.form["stylist_id"])
    date = request.form["date"]
    time = request.form["time"]

    # 予約登録を実行
    success = service.create_reservation(
        user_id=user_id,
        menu_ids=menu_ids,
        stylist_id=stylist_id,
        date=date,
        time=time,
    )

    if success: # 登録成功なら予約一覧へ移動
        return redirect(url_for("reservation_list"))

    return "この時間は予約できません", 400 # 同じ時間に予約がある場合

# --------------------
# 予約キャンセル
# --------------------
@app.route("/reservation/cancel", methods=["POST"])
def cancel_reservation():

    reservation_id = int(request.form["reservation_id"]) # フォームから予約IDを取得

    service = ReservationService() # 予約サービスを利用

    service.cancel_reservation(reservation_id) # 予約をキャンセル

    return redirect(url_for("reservation_list")) # 予約一覧画面へ戻る

# --------------------
# ログイン
# --------------------
@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html") # TODO: POST時にAuthServiceで認証

# --------------------
# 会員登録
# --------------------
@app.route("/register", methods=["GET","POST"])
def register():
    return render_template("register.html") # TODO: POST時にAuthServiceで認証


# --------------------
# ログアウト
# --------------------
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# --------------------
# 履歴
# --------------------
# @app.route("/history")
# def history():

#     service = HistoryService()

#     histories = service.get_history(
#         session["user_id"]
#     )

#     return render_template(
#         "history.html",
#         histories=histories
#     )

if __name__ == "__main__": # python main.py で実行されたときだけサーバーを起動
    app.run(debug=True) # コードを保存すると自動で再起動