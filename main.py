from openai import OpenAI
from secret_data import CHATGPT_API_KEY


client = OpenAI(api_key=CHATGPT_API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "What is Machine Learning?",
        }
    ],
)

print(completion.choices[0].message)