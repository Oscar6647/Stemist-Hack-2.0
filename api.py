# Written by Juan Pablo Gutiérrez
from revChatGPT.V1 import Chatbot
from decouple import config

chatbot = Chatbot(config={
  "access_token": config("Token")
})

while True:
    prompt = input("You: ")
    if prompt == "exit":
        break
    print("Chatbot: ")
    for data in chatbot.ask(prompt):
        message = data["message"]
    print(message)
    