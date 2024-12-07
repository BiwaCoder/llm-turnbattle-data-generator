# LLM TurnBattle Data Generator

ターン制のRPGのゲームのキャラクターデータを動的に生成するAPIサービスです。
OpenAI APIを活用して、バランスの取れたプレイヤーと敵キャラクターのデータを自動生成します。

## 特徴

OpenAI APIを活用した動的なゲームデータ生成

FlaskベースのRESTful API

プレイヤーと敵キャラクターの自動バランス調整

柔軟なデータ出力形式（JSON）

エラーハンドリングとログ機能


## 必要なパッケージのインストール
pip install flask flask-cors openai

## 環境変数の設定
export OPENAI_API_KEY=your_api_key_here

※試したのはmacのみ

# 使用方法
サーバーの起動

python app.py

APIエンドポイント

GET /start: 新しいゲームデータを生成

# レスポンス例:
```

jsonCopy{
    "Player": {
        "Name": "Hero",
        "HP": 100,
        "Attack": 20,
        "Defense": 10
    },
    "Enemy": {
        "Name": "Slime",
        "HP": 80,
        "Attack": 15,
        "Defense": 5
    }
}
```



#プロジェクト構造
```
Copyproject/
├── app.py                 # メインアプリケーション
├── game_data_generator.py # ゲームデータ生成ロジック
├── game_routes.py        # APIルート定義
├── llm_interface.py      # OpenAI API インターフェース
└── data/
    └── initial_game_data.json
```
