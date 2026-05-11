import json

from sklearn.metrics.pairwise import cosine_similarity

from ai.embedder import get_embedding


with open("data/profile.json", "r") as f:

    profile = json.load(f)


profile_text = " ".join(

    profile["skills"]
    + profile["interests"]
    + profile["preferred_roles"]

)

profile_embedding = (
    get_embedding(profile_text)
)


def score_job(job):

    job_text = (

        job["title"]
        + " "
        + job["type"]
        + " "
        + job.get("description", "")

    )

    job_embedding = (
        get_embedding(job_text)
    )

    similarity = cosine_similarity(
        [profile_embedding],
        [job_embedding]
    )[0][0]

    return round(similarity * 100, 2)