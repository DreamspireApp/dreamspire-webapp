from fastapi import FastAPI
from pydantic import BaseModel
import os, requests

app = FastAPI()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_ID_TEXT=
os.getenv("MODEL_ID_TEXT")
MODEL_ID_IMAGE =
os.getenv("MODEL_ID_IMAGE")

class UserInput(BaseModel):
  text: str
  generate image: bool = False

@app.post("/chat")
def chat(input: UserInput):
  #Text generation
  text_res = requests.post(

f"https://api-inference.huggingface.co/models/{MODEL_ID_TEXT}",
    headers={"Authorisation":
f"Bearer {HF_TOKEN}"},
    json={"inputs": input.text}
  ).json()
  story = text_res[0]
["generated_text"] if
isinstance(text_res, list) else
text_res

  #Image generation (optional)
  image_url = None
  if input.generate_image:
    img_res = requests.post(

f"https://api-inference.huggingface.co/models/{MODEL_ID_IMAGE}",
      headers={"Authorisation":
f"Bearer {HF_TOKEN}"},
      json={"inputs": story}
    )
    image_url = img_res.content

    return {"text": story, "image":
image_url}
