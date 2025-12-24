@app.post("/chat")
def chat(request: ChatRequest):
    if not HF_API_KEY:
        return {"reply": "AI service is not configured properly."}

    prompt = f"""
You are a health assistant.
Rules:
- Do NOT diagnose diseases
- Give only general health information
- Be calm and supportive
- Suggest consulting a doctor if symptoms persist

User: {request.message}
Assistant:
"""

    try:
        response = requests.post(
            HF_URL,
            headers=HEADERS,
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 150,
                    "temperature": 0.7
                }
            },
            timeout=25  # ⬅️ IMPORTANT
        )

        if response.status_code != 200:
            return {
                "reply": (
                    "I'm currently experiencing high traffic. "
                    "Please try again in a few moments."
                )
            }

        result = response.json()

        ai_text = result[0]["generated_text"]
        ai_reply = ai_text.split("Assistant:")[-1].strip()

        return {"reply": ai_reply}

    except requests.exceptions.Timeout:
        return {
            "reply": (
                "The AI is taking longer than usual to respond. "
                "Please try again shortly."
            )
        }

    except Exception:
        return {
            "reply": (
                "Something went wrong while generating a response. "
                "Please try again."
            )
        }
