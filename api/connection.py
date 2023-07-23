from revChatGPT.V1 import Chatbot
from decouple import config
import execjs


chatbot = Chatbot(config={
  "access_token": config("Token")
})

# Create a function that receives a prompt and returns a response
def ask(prompt):
    with open('api/mongo/upload.js', 'r') as file:
        js_code = file.read()

    context = execjs.compile(js_code)

    # Call the JavaScript function with the parameter

    if prompt == "exit":
        return
    print("Chatbot: ")
    for data in chatbot.ask(prompt):
        message = data["message"]
    # Catch the error
    try:
        context.call("uploadGPTResult", message).then(print)
    except Exception as e :
        print(e)
    
    return message
