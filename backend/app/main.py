from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "AI Health Assistant Backend is Live"
    }

@app.get("/health")
def health_check():
    return {"health": "OK"}
