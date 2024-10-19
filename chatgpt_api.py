import os
from openai import OpenAI
from secret_data import CHATGPT_API_KEY

from dotenv import load_dotenv


load_dotenv()
model = os.getenv('model')

def use_chatgpt(question):
    client = OpenAI(api_key=CHATGPT_API_KEY)

    response = client.chat.completions.create(
        model=f'{model}',
        messages=[
            {
                'role': 'user',
                'content': f'{question}',
            }
        ],
    )

    return response.choices[0].message.content