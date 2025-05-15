from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/generate")
async def generate_post(request: Request):
    data = await request.json()
    topic = data.get("topic", "daily life")

    prompt = f"Write a short, catchy social media post about '{topic}'. Keep it under 280 characters."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"post": response['choices'][0]['message']['content'].strip()}

@app.get("/", response_class=HTMLResponse)
async def serve_homepage():
    with open("index.html", "r") as f:
        return f.read()
