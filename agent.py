import os

import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL_CANDIDATES = ["gemma3:1b", "llama3.2:3b", "qwen2.5:3b", "gemma3:4b"]

with open("knowledge/health_info.txt", "r", encoding="utf-8") as file:
    HEALTH_INFO = file.read().strip()


def fallback_answer(question: str) -> str:
    q = question.lower()

    if "headache" in q:
        return (
            "Headaches can happen with dehydration, poor sleep, stress, or other health conditions. "
            "Rest, drink enough water, and avoid triggers when possible. Seek urgent medical care if the headache is sudden, severe, or comes with confusion, weakness, or a seizure."
        )
    if "sleep" in q:
        return (
            "Good sleep habits include a consistent bedtime, less screen time before bed, and a calm routine. "
            "Aim for regular sleep and wake times, and avoid heavy meals or caffeine late in the day."
        )
    if "hydration" in q or "water" in q:
        return (
            "Staying hydrated helps your energy, concentration, and overall body function. Signs of dehydration can include thirst, dry mouth, dizziness, or dark urine. Drink water regularly and seek care if symptoms worsen."
        )
    if "nutrition" in q or "food" in q:
        return (
            "A balanced diet with fruits, vegetables, protein, and whole grains supports better health. Try to eat regular meals and limit excess sugar and processed foods when possible."
        )
    return (
        "I can help with general health awareness, such as healthy habits, common symptoms, and basic self-care tips. "
        "For serious concerns or persistent symptoms, it is best to consult a healthcare professional."
    )


def ask_agent(user_question):
    question = (user_question or "").strip()
    if not question:
        return "Please enter a health-related question."

    prompt = f"""
You are Swasthya Sahayak, a health awareness assistant.

Use this trusted health information:
{HEALTH_INFO}

Answer in 3 to 5 short sentences max.
If the question is unrelated to health, say you can only help with general health awareness.
Never diagnose a disease or prescribe medicine.

User question: {question}
"""

    last_error = None
    for model in MODEL_CANDIDATES:
        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.2,
                        "num_predict": 120,
                        "top_k": 20,
                        "top_p": 0.9,
                    },
                },
                timeout=20,
            )
            response.raise_for_status()
            payload = response.json()

            if payload.get("error"):
                raise ValueError(payload["error"])

            answer = payload.get("response", "").strip()
            if answer:
                return answer

        except (requests.RequestException, ValueError, KeyError) as exc:
            last_error = exc
            continue

    return fallback_answer(question) if last_error else "The health assistant is unavailable right now."