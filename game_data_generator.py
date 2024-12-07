import json
import logging
import re
from llm_interface import LLMInterface


class GameDataGenerator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.llm = LLMInterface()

    def generate_balanced_game_data(self):
        """
        LLM を使用してバランスの取れたゲームデータを生成する
        """
        prompt = """
        シンプルなRPGゲーム用のJSONデータを生成してください。以下の条件を満たしてください:
        - プレイヤーと敵が交互に攻撃するターン制バトルです。
        - プレイヤーと敵のどちらかが3回攻撃することでギリギリ勝敗が決まるように調整してください。
        - プレイヤーにはわずかに勝つ可能性があるように設定してください。
        - 各キャラクターには以下のステータスを含めてください:
            - HP: ヒットポイント
            - Attack: 攻撃力
            - Defense: 防御力
        解説はつけずjsonだけを出力してください。
        - JSON形式で出力してください。例:
        {
            "Player": {
                "Name": "Hero",
                "HP": 100,
                "Attack": 20,
                "Defense": 10
            },
            "Enemy": {
                "Name": "Slime",
                "HP": 80,
                "Attack": 25,
                "Defense": 8
            }
        }
        """

        system_message = "あなたはゲームバランス設計の専門家です。指定された条件を満たすゲームデータを作成してください。解説はつけずjsonだけを出力してください。"

        try:
            self.logger.debug("Requesting data from LLM")
            response = self.llm.generate_response(prompt, system_message)

            # レスポンス内容をログに記録
            self.logger.debug(f"LLM Response: {response}")

            # 余分な囲み文字やコードブロックを削除
            cleaned_response = self._clean_response(response)
            self.logger.debug(f"Cleaned LLM Response: {cleaned_response}")

            # JSON のデコード
            game_data = json.loads(cleaned_response)
            return game_data

        except json.JSONDecodeError as e:
            self.logger.error(f"JSONDecodeError: {e}\nレスポンス内容: {response}", exc_info=True)
            raise ValueError("LLM から返されたデータが正しい JSON 形式ではありません。")
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}", exc_info=True)
            raise RuntimeError(f"データ生成中にエラーが発生しました: {e}")

    def _clean_response(self, response):
        """
        LLM レスポンスから余分な文字列や囲み記号を削除する
        """
        # JSONコードブロック（```json ... ```）を削除
        cleaned = re.sub(r"```(?:json)?", "", response)
        cleaned = cleaned.replace("```", "").strip()
        return cleaned
