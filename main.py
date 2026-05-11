import json

from ai.scorer import score_job

from notifier.telegram_bot import (
    send_job_alert
)

from ai.outreach import (
    generate_outreach
)

from ai.recruiter_finder import (
    generate_recruiter_search
)

from scrapers.yc import (
    scrape_yc_jobs
)

from scrapers.wellfound import (
    scrape_wellfound_jobs
)


yc_jobs = scrape_yc_jobs()

wellfound_jobs = (
    scrape_wellfound_jobs()
)


jobs = yc_jobs + wellfound_jobs


unique_jobs = []

seen_links = set()


for job in jobs:

    if job["link"] not in seen_links:

        unique_jobs.append(job)

        seen_links.add(job["link"])


with open("data/jobs.json", "w") as f:

    json.dump(
        unique_jobs,
        f,
        indent=4
    )


print("\nTOTAL UNIQUE JOBS:")
print(len(unique_jobs))


print("\nAI MATCH SCORES:\n")


for job in unique_jobs[:10]:

    score = score_job(job)

    print(f"\nJob: {job['title']}")

    print(f"Type: {job['type']}")

    print(f"Source: {job['source']}")

    print(f"Match Score: {score}%")

    outreach = generate_outreach(job)

    print("\nOUTREACH MESSAGE:\n")

    print(outreach)

    recruiter_links = (
        generate_recruiter_search(job)
    )

    print("\nRECRUITER SEARCH:\n")

    print(
        recruiter_links[
            "linkedin_search"
        ]
    )

    print("-" * 50)

    if score > 40:

        send_job_alert(job, score)