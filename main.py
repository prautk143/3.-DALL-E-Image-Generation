from boltiotai import openai
import os

api_key = os.environ['API_KEY']

openai.api_key = api_key

response = openai.Images.create(
  prompt="MS dhoni with bat",
  model="dall-e-3",
  n=1,
  size="1024x1024")

print(response["data"][0]["url"])
