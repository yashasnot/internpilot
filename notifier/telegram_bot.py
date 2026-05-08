import requests
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_job_alert(job, score):

    message = f"""
🔥 Internship Match Found

💼 Role:
{job['title']}

🏷 Type:
{job['type']}

📊 Match Score:
{round(score, 2)}%

🔗 Link:
{job['link']}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)