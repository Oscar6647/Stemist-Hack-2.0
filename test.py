import openai
from decouple import config

openai.organization = "org-Xp6dWNZIKaKPkOGF5UhdhtG8"
openai.api_key = config('OPEN_AI')

print(openai.Model.list())

openai.File.create(
    file = open("testdata.jsonl","rb"),
    purpose = 'fine-tune'
)
