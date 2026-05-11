from playwright.sync_api import sync_playwright


def scrape_wellfound_jobs():

    jobs = []

    keywords = [
        "intern",
        "machine learning",
        "ai",
        "artificial intelligence",
        "data",
        "research",
        "fintech",
        "quant",
        "trading",
        "analytics",
        "python"
    ]

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            "https://wellfound.com/jobs"
        )

        page.wait_for_timeout(7000)

        links = page.locator("a")

        count = links.count()

        print(f"\nWELLFOUND LINKS FOUND: {count}\n")

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
                            "https://wellfound.com"
                            + href
                        )

                    job_type = "general"

                    lower_text = text.lower()

                    if any(word in lower_text for word in [
                        "ai",
                        "machine learning",
                        "data",
                        "research"
                    ]):
                        job_type = "ai/ml"

                    elif any(word in lower_text for word in [
                        "fintech",
                        "quant",
                        "trading",
                        "analytics"
                    ]):
                        job_type = "fintech"

                    jobs.append({
                        "title": text,
                        "link": full_link,
                        "type": job_type,
                        "description": text,
                        "source": "wellfound"
                    })

            except:

                pass

        browser.close()

    return jobs