#__________________________________________
'''
Input to the model can be string / message
input types: 1. text prompts, 2. message prompts, 3. Dictonary format
message: 
    - fundametal unit of context
    - represent input or output of models
    - contains - role, content, metadata

    Message Types:
        1. System message: 
        2. Human Message: 
        3. AIMessage: 
        4. ToolMessage: 

        SYSTEM MESSAGE:
            * A SystemMessage represent an initial set of instructions that primes the model’s behavior. 
            * You can use a system message to set the tone, define the model’s role, and establish guidelines for responses.

        HUMAN MESSAGE:
            * A HumanMessage represents user input and interactions. 
            * They can contain text, images, audio, files, and any other amount of multimodal content.
        AI MESSAGE:
            * Output of the model.

    ======> MESSAGE CONTENT <======
    * Messages have the content type which is loosely types.
    * Messages content may contains 
        1. Text
            # String content
            human_message = HumanMessage("Hello, how are you?")
        
        2. list of content blocks (native providers)
            # Provider-native format (e.g., OpenAI)
            human_message = HumanMessage(
                content=[
                    {"type": "text", "text": "Hello, how are you?"},
                    {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
                ])
        
        3. list of langchain's standard content blocks
            # List of standard content blocks
            human_message = HumanMessage(
            content_blocks=[
                {"type": "text", "text": "Hello, how are you?"},
                {"type": "image", "url": "https://example.com/image.jpg"},
                ])

            Types:
                a. text content block: {"type": "text", "text": "text content" }
                b. reasoning content block:
                    {
                    "type": "reasoning",
                    "reasoning": "The user is asking about...",
                    "extras": {"signature": "abc123"},
                    }
                c. mulitmodal:
                    1. 
                            {
                        "type": "image/audio/video/file/",
                        "url": "url link",
                        "base64": "",
                        "id": "",
                        "mime_type": "", # ex: image/jpeg, image/png, audio/mpeg, audio/wav, video/mp4, video/webm, application/pdf,
                        } 
                    2. tool_call
                        {
                            "type": "tool_call",
                            "name": "search",
                            "args": {"query": "weather"},
                            "id": "call_123"
                        }
                    3. ToolCallChunk: Streaming tool call fragment
                        {
                            "type": "tool_call_chunk",
                            "name": "search",
                            "args": {"query": "weather"},
                            "id": "call_123" 
                            "index": "" (number or string) <--- position of string.
                        }
                    4. invalid tool call:
                d. server side tool execution:
                    1. server tool call:
                        {
                            "type": "server_tool_call",
                            "id": "",<---An identifier associated with the tool call.
                            "name": "",
                            "args": "",
                        }
                    2. ServerToolCallChunk
                    3. ServerToolResult
                    

'''
#______________ human_message and system_message {start}______________

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyBboEwNTj2QbX30NBvy9eeESvV7Ukm3ODc"
model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider = "google_genai"
    )

# sys_message = SystemMessage(
#                         """
#                         You are Generative AI application developer and you have good expertise in Langchain family with python.                 
#                         """
#                             )
# human_message = HumanMessage(
#                         """
#                         Give the what are message types in langchain in short
#                         """
#                         )

# messages = [
#     sys_message,
#     human_message
# ]

# response = model.invoke(messages)
# print(response)

#_______________ human_message and system_message {end} ________________________

#_____________________ all types except **tool message** ________________________

from langchain.messages import SystemMessage, HumanMessage, AIMessage

message = [
    SystemMessage("""You are a helpfull assistant"""),
    HumanMessage("""Will you help me?"""),
    AIMessage("""I am happy to help"""),
    HumanMessage("""what is multiplication of 3 and 10?""")
]

response = model.invoke(message)
print(response)

#_____________________________________________________________________