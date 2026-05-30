import json
from datetime import datetime


APPLICATION_FILE = "data/applications.json"


def load_applications():

    try:

        with open(
            APPLICATION_FILE,
            "r"
        ) as f:

            return json.load(f)

    except:

        return []


def save_applications(data):

    with open(
        APPLICATION_FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def add_application(
    company,
    role
):

    apps = load_applications()

    apps.append({

        "company": company,

        "role": role,

        "status": "Applied",

        "date": str(
            datetime.now().date()
        )

    })

    save_applications(apps)

    print(
        "Application saved."
    )


def show_applications():

    apps = load_applications()

    for app in apps:

        print(
            f"{app['company']} | "
            f"{app['role']} | "
            f"{app['status']}"
        )