import prompter 
from pdfminer.high_level import extract_text
from connection import ask

prompt = """
    The following file is a class study plan. Please provide some recommendations considering the following information:
"""

subjet = input("What is the subject of the class study plan?")
subtopic = input("What is the subtopic of the class study plan? ")
time = input("How long does the class last? ")
age = input("What is the age of the students? ")

#map subject to subject enum

text = extract_text("api/example.pdf")

prompt += text

print(ask(prompt))