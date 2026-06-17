from dotenv import load_dotenv
import requests
from fastapi import FastAPI
import os
last_update_id = 0
load_dotenv()
app = FastAPI()
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

    return response.json()
    
def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url)

    return response.json()


@app.get("/send/{message}")
def notify(message: str):
    result = send_telegram_message(
        message
    )

    return {
        "status": "success",
        "telegram_response": result
    }
