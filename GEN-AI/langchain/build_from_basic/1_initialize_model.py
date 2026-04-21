'''
input ---> LLM ---> output
'''

from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider = "google_genai"
    )
response = model.invoke("what is langchain? Give a short summary?")
# response type : <class 'langchain_core.messages.ai.AIMessage'>

print(response)