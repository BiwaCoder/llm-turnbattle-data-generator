from flask import Blueprint, jsonify
from game_data_generator import GameDataGenerator
import logging

# ログを設定
logger = logging.getLogger(__name__)

# ルートをまとめる Blueprint を定義
game_routes = Blueprint('game_routes', __name__)

# GameDataGenerator のインスタンスを初期化
data_generator = GameDataGenerator()

@game_routes.route('/start', methods=['GET'])
def start_game():
    """
    LLM を使用してゲームデータを生成し、返します。
    """
    try:
        game_data = data_generator.generate_balanced_game_data()
        return jsonify(game_data)
    except Exception as e:
        # エラーログをターミナルに出力
        logger.error(f"Error in /start endpoint: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500

def create_routes(app):
    """
    Flask アプリケーションにルートを登録する
    """
    app.register_blueprint(game_routes)
