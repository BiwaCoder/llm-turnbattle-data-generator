import openai
import os

class LLMInterface:
    def __init__(self):
        """
        OpenAI API クライアントの初期化
        """
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("環境変数 'OPENAI_API_KEY' が設定されていません。")
        self.client = openai.OpenAI(api_key=api_key)

    def generate_response(self, prompt, system_message):
        """
        指定されたプロンプトとシステムメッセージを用いて応答を生成
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",  # モデル名を修正
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content  # 修正済み
        except Exception as e:
            raise RuntimeError(f"LLM の応答生成中にエラーが発生しました: {e}")
