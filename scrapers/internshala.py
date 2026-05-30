from playwright.sync_api import sync_playwright


def scrape_internshala_jobs():

    jobs = []

    keywords = [
        "intern",
        "machine learning",
        "ai",
        "artificial intelligence",
        "data science",
        "analytics",
        "fintech",
        "python",
        "research"
    ]

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            "https://internshala.com/internships/"
        )

        page.wait_for_timeout(7000)

        links = page.locator("a")

        count = links.count()

        print(
            f"\nINTERNSHALA LINKS FOUND: {count}\n"
        )

        for i in range(count):

            try:

                text = (
                    links.nth(i)
                    .inner_text()
                    .strip()
                )

                href = (
                    links.nth(i)
                    .get_attribute("href")
                )

                if (
                    text
                    and href
                    and any(
                        keyword in text.lower()
                        for keyword in keywords
                    )
                ):

                    full_link = href

                    if href.startswith("/"):

                        full_link = (
                            "https://internshala.com"
                            + href
                        )

                    lower_text = text.lower()

                    job_type = "general"

                    if any(word in lower_text for word in [
                        "ai",
                        "machine learning",
                        "data science",
                        "research"
                    ]):

                        job_type = "ai/ml"

                    elif any(word in lower_text for word in [
                        "fintech",
                        "analytics",
                        "trading"
                    ]):

                        job_type = "fintech"

                    jobs.append({

                        "title": text,

                        "link": full_link,

                        "type": job_type,

                        "description": text,

                        "source": "internshala"

                    })

            except:

                pass

        browser.close()

    return jobs