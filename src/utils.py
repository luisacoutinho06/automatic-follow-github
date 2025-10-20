import requests

GITHUB_API = "https://api.github.com"


def make_headers(token, agent="auto-cli"):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": agent
    }


def get_all_followers(headers, username):
    followers = []
    url = f"{GITHUB_API}/users/{username}/followers"
    params = {"per_page": 100, "page": 1}

    while True:
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code != 200:
            print(f"Error fetching followers: {resp.status_code}")
            break

        data = resp.json()
        if not data:
            break

        followers.extend([u["login"] for u in data])

        if "next" in resp.links:
            params["page"] += 1
        else:
            break

    return followers


def get_following(headers, username):
    following = []
    url = f"{GITHUB_API}/users/{username}/following"
    params = {"per_page": 100, "page": 1}

    while True:
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code != 200:
            print(f"Error fetching following: {resp.status_code}")
            break

        data = resp.json()
        if not data:
            break

        following.extend([u["login"] for u in data])

        if "next" in resp.links:
            params["page"] += 1
        else:
            break

    return following
