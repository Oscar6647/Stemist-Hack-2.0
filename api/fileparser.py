from pdfminer.high_level import extract_text
from connection import ask

prompt = """
    The following file is a class study plan. Please provide some recommendations
    for the teacher to improve their class study plan:
"""
text = extract_text("api/example.pdf")

prompt += text

print(ask(prompt))