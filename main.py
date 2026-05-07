import json

from ai.scorer import score_job


with open("data/jobs.json", "r") as f:
    jobs = json.load(f)


print("\nAI MATCH SCORES:\n")


for job in jobs[:10]:

    score = score_job(job)

    print(f"{job['title']}")
    print(f"Type: {job['type']}")
    print(f"Match Score: {score}%")
    print(job["link"])

    print("-" * 50)