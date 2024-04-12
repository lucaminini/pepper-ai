import requests
import json
import os


class OpenAIapi:
    url = "https://api.openai.com/v1/chat/completions"

    def __init__(self, api_key, openai_model, chat_file, max_messages):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(api_key)
        }
        self.model = openai_model
        self.chat_file = chat_file

        self.max_messages = max_messages

        if not os.path.exists(chat_file):
            with open(chat_file, 'w') as x:
                json.dump([], x)

    def delete_chat(self):
        if not os.path.exists(self.chat_file):
            with open(self.chat_file, 'w') as x:
                json.dump([], x)

    def llm(self, role, query):
        with open(self.chat_file, 'r') as x:
            old_messages = json.load(x)

        old_messages = old_messages[-self.max_messages:]

        data = {
            "model": self.model,
            "messages": old_messages + [
                {
                    "role": role,
                    "content": query
                }
            ]
        }

        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        if response.status_code != 200:
            return None

        response_json = response.json()
        old_messages.append({"role": role, "content": query})
        old_messages.append({"role": response_json[u'choices'][0][u'message'][u'role'],
                             "content": response_json[u'choices'][0][u'message'][u'content']})

        with open(self.chat_file, 'w') as x:
            json.dump(old_messages, x, indent=4)

        return response_json[u'choices'][0][u'message'][u'content']