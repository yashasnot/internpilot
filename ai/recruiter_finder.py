import urllib.parse


def generate_recruiter_search(job):

    title = job["title"]

    query = (
        f"{title} recruiter LinkedIn"
    )

    encoded_query = urllib.parse.quote(
        query
    )

    google_url = (
        "https://www.google.com/search?q="
        + encoded_query
    )

    linkedin_query = urllib.parse.quote(
        f"{title} recruiter site:linkedin.com"
    )

    linkedin_search_url = (
        "https://www.google.com/search?q="
        + linkedin_query
    )

    return {
        "google_search": google_url,
        "linkedin_search": linkedin_search_url
    }