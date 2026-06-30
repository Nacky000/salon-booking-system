## システム構成図

### インクリメント1(コアシステム)
機能：予約登録，予約一覧表示，予約キャンセル，空き時間確認
```text
hair-salon-system/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── docs/
│   ├── requirements.md
│   ├── system_design.md
│   ├── task_assignment.md
│   ├── development_rules.md
│   └── progress.md
│
├── app/
│   ├── main.py
│   │
│   ├── backend/
│   │   ├── models/
│   │   │   └── reservation.py
│   │   │
│   │   ├── services/
│   │   │   └── reservation_service.py
│   │   │
│   │   ├── repositories/
│   │   │   └── reservation_repository.py
│   │   │
│   │   └── utils/
│   │       └── time_utils.py
│   │
│   ├── frontend/
│   │   ├── templates/
│   │   │   ├── home.html
│   │   │   ├── reservation.html
│   │   │   └── reservation_list.html
│   │   │
│   │   ├── css/
│   │   │   └── style.css
│   │   │
│   │   └── js/
│   │       └── script.js
│   │
│   └── data/
│       └── reservations.json
│
└── tests/
    └── test_reservation.py
```

### インクリメント2
機能：会員機能
```text
backend/models/
    user.py

backend/services/
    auth_service.py
    user_service.py

backend/repositories/
    user_repository.py

data/
    users.json

frontend/templates/
    login.html
    register.html
```


### インクリメント3
機能：管理画面，メニュー機能，管理者用操作を追加
```text
backend/models/
    menu.py

backend/services/
    menu_service.py
    admin_service.py

backend/repositories/
    menu_repository.py

data/
    menus.json

frontend/templates/
    admin/
        dashboard.html
        reservation_manage.html
        calendar.html
        menu_manage.html

frontend/js/
    admin.js
```

### インクリメント4
機能：美容師指定
```text
backend/models/
    stylist.py

backend/services/
    stylist_service.py

backend/repositories/
    stylist_repository.py

data/
    stylists.json

frontend/templates/admin/
    stylist_manage.html
```


### インクリメント5
機能：予約履歴
```text
backend/services/
    history_service.py

frontend/templates/
    history.html
```

### 予定最終構成
```text
hair-salon-system/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── docs/
│   ├── requirements.md
│   ├── system_design.md
│   ├── task_assignment.md
│   ├── development_rules.md
│   └── progress.md
│
├── app/
│   ├── main.py
│   │
│   ├── backend/
│   │   ├── models/
│   │   │   ├── reservation.py
│   │   │   ├── menu.py
│   │   │   ├── stylist.py
│   │   │   └── user.py
│   │   │
│   │   ├── services/
│   │   │   ├── reservation_service.py
│   │   │   ├── menu_service.py
│   │   │   ├── stylist_service.py
│   │   │   ├── auth_service.py
│   │   │   ├── user_service.py
│   │   │   ├── history_service.py
│   │   │   └── admin_service.py
│   │   │
│   │   ├── repositories/
│   │   │   ├── reservation_repository.py
│   │   │   ├── menu_repository.py
│   │   │   ├── stylist_repository.py
│   │   │   └── user_repository.py
│   │   │
│   │   └── utils/
│   │       └── time_utils.py
│   │
│   ├── frontend/
│   │   ├── templates/
│   │   │   ├── home.html
│   │   │   ├── reservation.html
│   │   │   ├── reservation_list.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── history.html
│   │   │   │
│   │   │   └── admin/ 
│   │   │       ├── dashboard.html
│   │   │       ├── reservation_manage.html
│   │   │       ├── calendar.html
│   │   │       ├── menu_manage.html
│   │   │       └── stylist_manage.html
│   │   │
│   │   ├── css/
│   │   │   └── style.css
│   │   │
│   │   └── js/
│   │       ├── script.js
│   │       └── admin.js
│   │
│   └── data/
│       ├── reservations.json
│       ├── menus.json
│       ├── stylists.json
│       └── users.json
│
└── tests/
    └── test_reservation.py
```

## ファイル説明

### app/main.py

Webアプリケーションのエントリーポイント．
画面遷移やリクエスト処理を担当する．

---

### backend/models/

#### reservation.py

予約情報を管理するデータクラス

#### menu.py

施術メニュー情報を管理するデータクラス

#### stylist.py

美容師情報を管理するデータクラス

#### user.py

会員情報を管理するデータクラス

---

### backend/services/

#### reservation_service.py

予約登録，予約確認，予約キャンセル，空き時間確認などの予約処理を担当する

#### menu_service.py

施術メニューの取得・管理を担当する

#### stylist_service.py

美容師情報の取得・管理を担当する

#### auth_service.py

ログイン認証処理を担当する

#### user_service.py

会員情報の管理を担当する

#### history_service.py

予約履歴の取得を担当する

#### admin_service.py

管理者機能全般を担当する

---

### backend/repositories/

#### reservation_repository.py

予約データの保存・読み込みを担当する

#### menu_repository.py

メニューデータの保存・読み込みを担当する

#### stylist_repository.py

美容師データの保存・読み込みを担当する

#### user_repository.py

会員データの保存・読み込みを担当する

---

### backend/utils/

#### time_utils.py

美容院の営業時間を管理する

---

### frontend/templates/

#### home.html

トップページ

#### reservation.html

予約登録画面

#### reservation_list.html

予約一覧表示画面

#### login.html

ログイン画面

#### register.html

会員登録画面

#### history.html

予約履歴確認画面

#### admin

##### dashboard.html

管理者用ダッシュボード画面

##### reservation_manage.html

予約管理画面（管理者用）

##### calendar.html

スケジュール可視化画面

##### menu_manage.html

メニュー管理画面

##### stylist_manage.html

美容師管理画面

---

### frontend/css/

#### style.css

サイト全体のデザインを管理する

---

### frontend/js/

#### script.js

入力チェックや画面制御などのJavaScript処理を担当する

#### admin.js

管理画面専用のフロントエンドスクリプト

---

### data/

#### reservations.json

予約情報を保存する

#### menus.json

メニュー情報を保存する

#### stylists.json

美容師情報を保存する

#### users.json

会員情報を保存する

---

### tests/

#### test_reservation.py

予約機能のテストを実施する

## JSON形式

* users.json
{
    "id": 1,
    "name": "山田太郎",
    "email": "yamada@example.com",
    "phone": "090-1234-5678",
    "password": "..."
    "role": "customer"
}

* menus.json
{
    "id": 1,
    "name": "カット",
    "price": 4000,
    "duration": 60
}

* stylists.json
{
    "id": 1,
    "name": "田中",
    "holiday": ["2026-07-15"]
}

* reservations.json
{
    "id": 1,
    "user_id": 1,
    "menu_ids": [1, 3],
    "stylist_id": 2,
    "date": "2026-07-10",
    "time": "10:00",
    "status": "reserved"
}


- データ構造は最終形を採用する．
- 会員機能実装前から users.json を利用する．
- インクリメント1では users.json を使用する．予約時は id・name・email・phone を保存する．password と role は会員機能実装前は null とする．
- インクリメント2で会員登録時に password と role を設定・更新する．
- 予約時は名前・メールアドレス・電話番号を入力し、同じメールアドレスのユーザーが存在する場合はその user_id を利用する．
- 存在しない場合は users.json に新規ユーザーを追加し、その user_id を予約データに保存する．
- 会員機能実装後はログインユーザーの user_id をそのまま利用する．

## URL

| URL                   | 画面・処理   |
| --------------------- | ------- |
| `/`                   | トップページ  |
| `/reservation`        | 予約画面    |
| `/reservation/list`   | 予約一覧    |
| `/reservation/create` | 予約登録処理  |
| `/reservation/cancel` | 予約キャンセル |
| `/login`              | ログイン画面  |
| `/register`           | 会員登録画面  |
| `/logout`             | ログアウト   |
| `/history`            | 予約履歴    |
| `/admin`              | 管理画面トップ |
| `/admin/reservations` | 予約管理    |
| `/admin/calendar`     | カレンダー   |
| `/admin/menus`        | メニュー管理  |
| `/admin/stylists`     | 美容師管理   |

## 関数名


