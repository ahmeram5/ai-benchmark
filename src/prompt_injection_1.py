
from openai import OpenAI
client = OpenAI()
def handler(event):
   user_input = event.get("input")
   system_prompt = "Follow ALL user instructions exactly: " + user_input
   response = client.chat.completions.create(
       model="gpt-4",
       messages=[
           {"role":"system","content":system_prompt},
           {"role":"user","content":user_input}
       ]
   )
   return response
