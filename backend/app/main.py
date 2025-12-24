import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Health Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_API_KEY = os.getenv("HF_API_KEY")

HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
HF_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"status": "AI backend running"}


@app.post("/chat")
def chat(request: ChatRequest):
    if not HF_API_KEY:
        return {"reply": "AI key not configured."}

    prompt = f"""
You are a health assistant.
Rules:
- Do NOT diagnose diseases
- Give only general health information
- Always suggest consulting a doctor if symptoms persist

User: {request.message}
Assistant:
"""

    response = requests.post(
        HF_URL,
        headers=HEADERS,
        json={"inputs": prompt, "parameters": {"max_new_tokens": 200}},
        timeout=60
    )

    if response.status_code != 200:
        return {"reply": "AI service is temporarily unavailable. Please try again."}

    result = response.json()

    ai_text = result[0]["generated_text"]
    ai_reply = ai_text.split("Assistant:")[-1].strip()

    return {"reply": ai_reply}
