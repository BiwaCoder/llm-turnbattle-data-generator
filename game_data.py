import json
import os

# データファイルのパスを指定
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'initial_game_data.json')

def load_game_data():
    """
    JSON ファイルから初期データを読み込む
    """
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)  # データを辞書型で返す
