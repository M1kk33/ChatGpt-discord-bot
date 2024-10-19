from openai import OpenAI
from secret_data import CHATGPT_API_KEY

def use_chatgpt(question):
    client = OpenAI(api_key=CHATGPT_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"{question}",
            }
        ],
    )

    return response.choices[0].message.content