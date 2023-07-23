import prompter 
from pdfminer.high_level import extract_text
from connection import ask

def run():
    
    prompt = """
        The following file is a class study plan. Please provide some recommendations considering the following information:
    """

    #map subject to subject enum

    text = extract_text("api/example.pdf")

    prompt += text

    print(ask(prompt))

run()