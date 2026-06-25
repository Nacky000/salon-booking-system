## システム構成図

### インクリメント1(コアシステム)
機能：予約登録，予約一覧表示，予約キャンセル，空き時間確認
```text
hair-salon-system/
│
├── README.md
├── .gitignore
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
│   │   └── repositories/
│   │       └── reservation_repository.py
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
機能：メニュー機能追加
```text
backend/models/
    menu.py

backend/services/
    menu_service.py

backend/repositories/
    menu_repository.py

data/
    menus.json
```

### インクリメント3
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
```

### インクリメント4
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
│   │   │   └── history_service.py
│   │   │
│   │   └── repositories/
│   │       ├── reservation_repository.py
│   │       ├── menu_repository.py
│   │       ├── stylist_repository.py
│   │       └── user_repository.py
│   │
│   ├── frontend/
│   │   ├── templates/
│   │   │   ├── home.html
│   │   │   ├── reservation.html
│   │   │   ├── reservation_list.html
│   │   │   ├── login.html
│   │   │   ├── history.html
│   │   │   └── register.html
│   │   │
│   │   ├── css/
│   │   │   └── style.css
│   │   │
│   │   └── js/
│   │       └── script.js
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

Webアプリケーションのエントリーポイント。
画面遷移やリクエスト処理を担当する。

---

### backend/models/

#### reservation.py

予約情報を管理するデータクラス。

#### menu.py

施術メニュー情報を管理するデータクラス。

#### stylist.py

美容師情報を管理するデータクラス。

#### user.py

会員情報を管理するデータクラス。

---

### backend/services/

#### reservation_service.py

予約登録、予約確認、予約キャンセル、空き時間確認などの予約処理を担当する。

#### menu_service.py

施術メニューの取得・管理を担当する。

#### stylist_service.py

美容師情報の取得・管理を担当する。

#### auth_service.py

ログイン認証処理を担当する。

#### user_service.py

会員情報の管理を担当する。

#### history_service.py

予約履歴の取得を担当する。

---

### backend/repositories/

#### reservation_repository.py

予約データの保存・読み込みを担当する。

#### menu_repository.py

メニューデータの保存・読み込みを担当する。

#### stylist_repository.py

美容師データの保存・読み込みを担当する。

#### user_repository.py

会員データの保存・読み込みを担当する。

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

---

### frontend/css/

#### style.css

サイト全体のデザインを管理する

---

### frontend/js/

#### script.js

入力チェックや画面制御などのJavaScript処理を担当する

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
