
from openai import OpenAI
client = OpenAI()
def generate(prompt):
   return client.chat.completions.create(
       model="gpt-4",
       messages=[{"role":"user","content":prompt}]
       # max_tokens intentionally missing
   )
