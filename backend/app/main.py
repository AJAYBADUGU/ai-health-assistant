from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Health Assistant")

# Enable CORS (needed for frontend ↔ backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"status": "AI backend running"}


@app.post("/chat")
def chat(request: ChatRequest):
    """
    Reliable, deterministic health assistant.
    This guarantees responses on free-tier hosting.
    """

    message = request.message.lower()

    if "headache" in message:
        return {
            "reply": (
                "Headaches can be caused by stress, dehydration, lack of sleep, "
                "eye strain, or prolonged screen time. Try resting in a quiet place, "
                "drinking water, and limiting screen exposure. If the headache "
                "persists, worsens, or occurs frequently, please consult a doctor."
            )
        }

    if "fever" in message:
        return {
            "reply": (
                "Fever is often a sign that the body is fighting an infection. "
                "Make sure to stay hydrated, rest well, and monitor your temperature. "
                "If the fever is high, lasts more than a couple of days, or is "
                "accompanied by severe symptoms, consult a healthcare professional."
            )
        }

    if "cold" in message or "cough" in message:
        return {
            "reply": (
                "Colds and coughs are usually caused by viral infections. Rest, "
                "warm fluids, and proper hydration can help relieve symptoms. "
                "If symptoms persist for several days or worsen, consult a doctor."
            )
        }

    if "tired" in message or "fatigue" in message:
        return {
            "reply": (
                "Feeling tired or fatigued can be due to lack of sleep, stress, "
                "poor nutrition, or dehydration. Ensure you get adequate rest, "
                "eat balanced meals, and drink enough water. If fatigue continues, "
                "consider consulting a healthcare professional."
            )
        }

    if "stomach" in message or "abdominal" in message:
        return {
            "reply": (
                "Stomach discomfort can result from indigestion, stress, or dietary "
                "issues. Try eating light meals, avoiding spicy foods, and staying "
                "hydrated. If pain is severe or persistent, consult a doctor."
            )
        }

    # Default response
    return {
        "reply": (
            "I can provide general health information based on your symptoms. "
            "Please describe how you are feeling in more detail. "
            "For serious or persistent issues, it is always best to consult "
            "a qualified healthcare professional."
        )
    }
