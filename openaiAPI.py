import requests
import json

OPENAI_API_KEY = ""

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(OPENAI_API_KEY)
}

oldMessages = [
{
            "role": "system",
            "content": "Tu sei un matematico"
        },
        {
            "role": "user",
            "content": "che numero ricordi?"
        },
        {
            "role": "assistant",
            "content": "mi ricordo il 456"
        },
]

data = {
    "model": "gpt-3.5-turbo",
    "messages": oldMessages + [
        {
            "role": "user",
            "content": "cosa ti ho chiesto prima? e cosa hai risposto?"
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
