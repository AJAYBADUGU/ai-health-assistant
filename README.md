🩺 AI Health Assistant

A full-stack web application that provides general health guidance through a conversational chat interface.
Built with React, FastAPI, and deployed using Vercel and Render.

⚠️ This application provides general health information only and does not replace professional medical advice.

🔗 Live Demo

Frontend (Web App): https://your-vercel-link.vercel.app

Backend (API): https://ai-health-assistant.onrender.com

📌 Features

💬 Chat-based health assistant interface

🎨 Modern glassmorphism UI (Tailwind CSS)

⚙️ FastAPI backend with REST API

🌐 Fully deployed (Frontend + Backend)

🛡️ Safety-first responses (no diagnosis)

🔄 Reliable responses on free-tier hosting

🏗️ Tech Stack
Frontend

React.js

Tailwind CSS

Fetch API

Deployed on Vercel

Backend

FastAPI

Pydantic

Python

Deployed on Render

🧠 Project Architecture
User (Browser)
   ↓
React Frontend (Vercel)
   ↓
FastAPI Backend (Render)
   ↓
Rule-based Health Logic
   ↓
Response shown in UI

🩺 How It Works

User enters a health-related query (e.g., headache, fever, fatigue)

Frontend sends the message to the backend /chat API

Backend processes the message using predefined health logic

A safe, general health response is returned

The response is displayed in the chat UI

⚠️ Disclaimer

This project does not diagnose diseases

It provides general health information only

Users are advised to consult a doctor for serious or persistent symptoms

📂 Project Structure
ai-health-assistant/
│
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   └── App.js
│   ├── package.json
│
└── README.md

🚀 Installation (Local Setup)
Backend
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

Frontend
cd frontend
npm install
npm start

🎯 Key Learnings

Full-stack development using React and FastAPI

REST API design and CORS handling

Cloud deployment on free-tier platforms

Handling real-world infrastructure limitations

Building reliable systems with graceful fallbacks

🧠 Interview Explanation (One-Liner)

“I built and deployed a full-stack AI Health Assistant using React and FastAPI, with a reliable rule-based backend to ensure consistent responses on free cloud infrastructure.”

📌 Future Enhancements

Integrate paid LLM APIs (OpenAI / Gemini)

Add chat history using MongoDB

Authentication and user profiles

Multi-language support

👤 Author

Ajay Badugu
B.Tech – AIML
GitHub: https://github.com/AJAYBADUGU