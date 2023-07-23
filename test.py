from revChatGPT.V1 import Chatbot
from decouple import config
chatbot = Chatbot(config={
  "access_token": config("Token")
})
prompt = input()
response = ""
for data in chatbot.ask(
  prompt
):
    response = data["message"]
print(response)