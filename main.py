from openAI_api import OpenAIapi
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

testElement = OpenAIapi(OPENAI_API_KEY, "gpt-3.5-turbo", "user_chat.json")
print(testElement.llm("user", "cosa ti ho chiesto prima?"))
