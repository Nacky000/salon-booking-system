from backend.services.reservation_service import ReservationService
from backend.services.admin_service import AdminService
from backend.services.history_service import HistoryService
from backend.services.user_service import UserService
from backend.services.menu_service import MenuService
from backend.services.stylist_service import StylistService
from backend.services.auth_service import AuthService
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend"
) # Flaskアプリ作成，設定

app.secret_key = "salon-booking-system" # 実用ではランダムな長い文字列とする

admin_service = AdminService()


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

    if "user_id" not in session:
        return redirect(url_for("login", next=request.path))

    menu_service = MenuService()
    stylist_service = StylistService()

    menus = menu_service.get_all()
    stylists = stylist_service.get_all()

    return render_template(
        "reservation.html",
        menus=menus,
        stylists=stylists
    )

# --------------------
# 予約一覧
# --------------------
@app.route("/reservation/list")
def reservation_list():

    if "user_id" not in session:
        return redirect(url_for("login", next=request.path))
    
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

    # ログイン確認
    if "user_id" not in session:
        return redirect(url_for("login"))

    service = ReservationService()

    # ログインユーザーのIDを使用
    user_id = session["user_id"]

    menu_ids = [int(menu_id) for menu_id in request.form.getlist("menu_ids")]
    stylist_id = int(request.form["stylist_id"])
    date = request.form["date"]
    time = request.form["time"]

    success = service.create_reservation(
        user_id=user_id,
        menu_ids=menu_ids,
        stylist_id=stylist_id,
        date=date,
        time=time,
    )

    if success:
        return redirect(url_for("reservation_list"))

    return "この時間は予約できません", 400

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
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        auth = AuthService()

        email = request.form["email"]
        password = request.form["password"]

        user = auth.login(email, password)

        if user is None:
            return "メールアドレスまたはパスワードが違います"

        # ログイン状態を保存
        session["user_id"] = user.user_id

        # 元の画面へ戻る
        next_page = request.args.get("next")

        if next_page:
            return redirect(next_page)

        # 指定がなければ予約画面へ
        return redirect(url_for("reservation"))

    return render_template("login.html")

# --------------------
# 会員登録
# --------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # パスワード確認
        if password != confirm_password:
            return "パスワードが一致しません", 400

        service = UserService()

        try:
            service.register_user(
                name,
                email,
                phone,
                password
            )

            return redirect(url_for("login"))

        except ValueError as e:
            return str(e), 400

    return render_template("register.html")


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
@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect(url_for("login", next=request.path))

    service = HistoryService()

    histories = service.get_history(session["user_id"])

    return render_template(
        "history.html",
        histories=histories
    )


# --------------------
# 管理画面トップ
# --------------------
@app.route("/admin")
def admin_dashboard():

    data = admin_service.get_dashboard_data()

    return render_template(
        "admin/dashboard.html",
        data=data
    )


# --------------------
# 会員一覧
# --------------------
@app.route("/admin/users")
def admin_users():

    users = admin_service.get_all_users()

    return render_template(
        "admin/users.html",
        users=users
    )

# --------------------
# メニュー一覧
# --------------------
@app.route("/admin/menus")
def admin_menus():

    menus = admin_service.get_all_menus()

    return render_template(
        "admin/menus.html",
        menus=menus
    )


# --------------------
# メニュー追加
# --------------------
@app.route("/admin/menu/add", methods=["POST"])
def admin_add_menu():

    name = request.form["name"]
    price = int(request.form["price"])
    duration = int(request.form["duration"])

    admin_service.add_menu(
        name,
        price,
        duration
    )

    return redirect(url_for("admin_menus"))


# --------------------
# メニュー更新
# --------------------
@app.route("/admin/menu/update", methods=["POST"])
def admin_update_menu():

    menu_id = int(request.form["menu_id"])
    name = request.form["name"]
    price = int(request.form["price"])
    duration = int(request.form["duration"])

    admin_service.update_menu(
        menu_id,
        name,
        price,
        duration
    )

    return redirect(url_for("admin_menus"))



# --------------------
# メニュー削除
# --------------------
@app.route("/admin/menu/delete", methods=["POST"])
def admin_delete_menu():

    menu_id = int(request.form["menu_id"])

    admin_service.delete_menu(menu_id)

    return redirect(url_for("admin_menus"))



# --------------------
# 美容師一覧
# --------------------
@app.route("/admin/stylists")
def admin_stylists():

    stylists = admin_service.get_all_stylists()

    return render_template(
        "admin/stylists.html",
        stylists=stylists
    )




# --------------------
# 美容師更新
# --------------------
@app.route("/admin/stylist/update", methods=["POST"])
def admin_update_stylist():

    stylist_id = int(request.form["stylist_id"])
    name = request.form["name"]
    holiday = request.form["holiday"]

    admin_service.update_stylist(
        stylist_id,
        name,
        holiday
    )

    return redirect(url_for("admin_stylists"))



# --------------------
# 美容師削除
# --------------------
@app.route("/admin/stylist/delete", methods=["POST"])
def admin_delete_stylist():

    stylist_id = int(request.form["stylist_id"])

    admin_service.delete_stylist(stylist_id)

    return redirect(url_for("admin_stylists"))


if __name__ == "__main__": # python main.py で実行されたときだけサーバーを起動
    app.run(debug=True) # コードを保存すると自動で再起動

