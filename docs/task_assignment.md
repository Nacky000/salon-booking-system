# 役割候補一覧（管理画面追加版）

---

## ① プロジェクト管理・設計

### 担当内容

* 要件定義書作成
* システム設計書作成
* タスク管理
* GitHub管理
* 進捗管理
* 開発ルール策定

### 関連ファイル

* docs/requirements.md
* docs/system_design.md
* docs/task_assignment.md
* docs/development_rules.md
* docs/progress.md


---

## ② フロントエンド（ユーザー画面）

### 担当内容

* ユーザー画面全般
* 予約・履歴・ログインUI

### 関連ファイル

* frontend/templates/home.html
* frontend/templates/reservation.html
* frontend/templates/reservation_list.html
* frontend/templates/login.html
* frontend/templates/register.html
* frontend/templates/history.html


---

## ③ フロントエンド（管理画面）

### 担当内容

* 管理画面UI
* カレンダーUI
* 管理操作画面

### 関連ファイル

* frontend/templates/admin/dashboard.html
* frontend/templates/admin/reservation_manage.html
* frontend/templates/admin/calendar.html
* frontend/templates/admin/menu_manage.html
* frontend/templates/admin/stylist_manage.html
* frontend/js/admin.js


---

## ④ UIデザイン

### 担当内容

* CSS設計
* UI統一
* レスポンシブ対応

### 関連ファイル

* frontend/css/style.css

---

## ⑤ フロントエンド（JavaScript）

### 担当内容

* 入力チェック
* ボタン制御
* エラーメッセージ表示
* フロント側処理実装

### 関連ファイル

* frontend/js/script.js

---

## ⑥ 予約機能

### 担当内容

* 予約登録
* 予約確認
* 予約キャンセル
* 空き時間確認

### 関連ファイル

* backend/models/reservation.py
* backend/services/reservation_service.py
* backend/repositories/reservation_repository.py
* data/reservations.json


---

## ⑦ メニュー機能

### 担当内容

* メニュー情報管理
* メニュー取得処理

### 関連ファイル

* backend/models/menu.py
* backend/services/menu_service.py
* backend/repositories/menu_repository.py
* data/menus.json


---

## ⑧ バックエンド（管理画面）

### 担当内容

* 予約・メニュー・美容師・会員情報の統合管理
* 管理画面用データ取得処理
* 予約ステータス変更
* 手動予約の追加・削除
* ダッシュボード集計処理
* 管理画面APIロジック

### 関連ファイル

* backend/services/admin_service.py


---

## ⑨ 美容師指定機能

### 担当内容

* 美容師情報管理
* 美容師指定処理

### 関連ファイル

* backend/models/stylist.py
* backend/services/stylist_service.py
* backend/repositories/stylist_repository.py
* data/stylists.json

---

## ⑩ 会員機能

### 担当内容

* 会員登録
* ログイン認証
* ユーザー情報管理

### 関連ファイル

* backend/models/user.py
* backend/services/auth_service.py
* backend/services/user_service.py
* backend/repositories/user_repository.py
* data/users.json
* frontend/templates/login.html
* frontend/templates/register.html

---

## ⑪ 予約履歴機能

### 担当内容

* 予約履歴表示
* 過去予約情報取得

### 関連ファイル

* backend/services/history_service.py
* frontend/templates/history.html


---

## ⑫ テスト・品質管理

### 担当内容

* 単体テスト
* 動作確認
* バグ管理
* 不具合修正

### 関連ファイル

* tests/test_reservation.py
* その他テストファイル

---

# 実装順

## STEP1
① プロジェクト管理・設計

## STEP2
⑥ 予約機能
② フロント（ユーザー）
④ UIデザイン
⑤ JavaScript

## STEP3
⑩ 会員機能

## STEP4
⑦ メニュー機能
⑧ 管理画面
③ フロント（管理画面）

## STEP5
⑨ 美容師指定

## STEP6
⑪ 履歴

## STEP7
⑫ テスト


# 担当割り当て

## 植木
- ①⑥⑫＋main.py

## 大塚
- ⑦⑧⑨⑩

## 砂子
- ②③④⑤⑪

* 担当番号のファイル以外触らないこと．
* main.pyには植木以外触らないこと．