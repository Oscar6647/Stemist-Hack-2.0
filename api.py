from revChatGPT.V1 import Chatbot
from decouple import config

chatbot = Chatbot(config={
  "access_token": config("Token")
})

# Create a function that receives a prompt and returns a response
def ask(prompt):
    if prompt == "exit":
        return
    print("Chatbot: ")
    for data in chatbot.ask(prompt):
        message = data["message"]
    return message
