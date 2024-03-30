from src.infra import mongo_database
import openai
import re


class GptIntegration:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.client = openai.OpenAI(
            api_key=api_key,
        )

    def extract_code(self, response):
        pattern_code = r'```(?:\w+\n)?(.*?)```'
        matches = re.findall(
            pattern_code, response.choices[0].message.content, re.DOTALL)
        if matches:
            return matches
        else:
            return None

    def send_message(self, problem: str, context: str = "analise de codigo"):
        openai.api_key = self.api_key
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": problem},
            ],
        )

        return response.choices[0].message.content
