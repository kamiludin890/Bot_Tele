from dotenv import load_dotenv
import requests
from fastapi import FastAPI
import os

load_dotenv()
app = FastAPI()
token = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

    return response.json()


@app.get("/")
def notify():
    result = send_telegram_message(
        "Ada request baru ke endpoint FastAPI!"
    )

    return {
        "status": "success",
        "telegram_response": result
    }