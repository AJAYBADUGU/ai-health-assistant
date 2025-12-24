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

Question: {request.message}
Answer:
"""

    try:
        response = requests.post(
            HF_URL,
            headers=HEADERS,
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 120,
                    "temperature": 0.5
                }
            },
            timeout=20
        )

        if response.status_code != 200:
            return {
                "reply": "The AI service is busy right now. Please try again shortly."
            }

        result = response.json()

        # ✅ FLAN-T5 RESPONSE FORMAT
        # result = [{ "generated_text": "..." }]
        if isinstance(result, list) and "generated_text" in result[0]:
            ai_reply = result[0]["generated_text"].strip()
        else:
            return {
                "reply": "I couldn't generate a response right now. Please try again."
            }

        return {"reply": ai_reply}

    except requests.exceptions.Timeout:
        return {
            "reply": "The AI is taking longer than usual. Please try again shortly."
        }

    except Exception as e:
        return {
            "reply": "Something went wrong while generating the response."
        }
