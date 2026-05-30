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

from scrapers.internshala import (
    scrape_internshala_jobs
)


print("\nSCRAPING YC JOBS...\n")

yc_jobs = scrape_yc_jobs()


print("\nSCRAPING WELLFOUND JOBS...\n")

wellfound_jobs = (
    scrape_wellfound_jobs()
)


print("\nSCRAPING INTERNSHALA JOBS...\n")

internshala_jobs = (
    scrape_internshala_jobs()
)


jobs = (

    yc_jobs

    + wellfound_jobs

    + internshala_jobs

)


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


try:

    with open(
        "data/seen_jobs.json",
        "r"
    ) as f:

        seen_jobs = json.load(f)

except:

    seen_jobs = []


seen_links_memory = set(seen_jobs)


print("\nTOTAL UNIQUE JOBS:")
print(len(unique_jobs))


print("\nAI MATCH SCORES:\n")


new_seen_links = []


for job in unique_jobs[:20]:

    score = score_job(job)

    print("\n========================")

    print(f"\nJob: {job['title']}")

    print(f"\nType: {job['type']}")

    print(f"\nSource: {job['source']}")

    print(f"\nMatch Score: {score}%")

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

    print("\n========================")


    if (
        score > 40
        and job["link"]
        not in seen_links_memory
    ):

        print("\nNEW JOB FOUND!")

        send_job_alert(job, score)

        new_seen_links.append(
            job["link"]
        )


updated_seen_jobs = (
    list(seen_links_memory)
    + new_seen_links
)


with open(
    "data/seen_jobs.json",
    "w"
) as f:

    json.dump(
        updated_seen_jobs,
        f,
        indent=4
    )


print("\nPROCESS COMPLETED.\n")