from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

with open("rag/data.txt", "r", encoding="utf-8") as f:
    content = f.read()

while True:
    question = input("你:")

    prompt = f"""
    请只根据以下资料回答问题。
    如果资料中没有答案，请说：资料中没有提到。

    资料：
    {content}

    问题：
    {question}
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是猫娘"},
            {"role": "user", "content": prompt}
        ]
    )

    print(response.choices[0].message.content)