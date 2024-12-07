from flask import Flask, jsonify
from flask_cors import CORS
from game_routes import create_routes
import logging

# ログの設定
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

# ルートを登録
create_routes(app)

# カスタムエラーハンドラーを追加
@app.errorhandler(Exception)
def handle_exception(e):
    # エラーログを出力
    app.logger.error(f"Unhandled Exception: {e}", exc_info=True)
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
