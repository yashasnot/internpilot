import json

from ai.scorer import score_job
from notifier.telegram_bot import send_job_alert


with open("data/jobs.json", "r") as f:
    jobs = json.load(f)


print("\nAI MATCH SCORES:\n")


for job in jobs[:10]:

    score = score_job(job)

    print(f"Job: {job['title']}")
    print(f"Type: {job['type']}")
    print(f"Match Score: {score}%")

    print("-" * 50)

    if score > 40:

        send_job_alert(job, score)