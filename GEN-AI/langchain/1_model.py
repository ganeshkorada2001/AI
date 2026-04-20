'''
_______________________________________________________________________
import os
from langchain.chat_models import init_chat_model
os.environ["GOOGLE_API_KEY"] = "A"
model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider = "google_genai"
    )
response = model.invoke("what is langchain? Give a short summary?")
# response type : <class 'langchain_core.messages.ai.AIMessage'>

print(response)
_______________________________________________________________________


______________________________INVOCATION_______________________________
1. model.invoke() : straightforward way to call a model with a single message or a list of messages.
2. model.stream() : 
3. model.batch()  : 
'''

