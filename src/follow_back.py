import requests
import json
import time
from pathlib import Path

GITHUB_API = "https://api.github.com"
STATE_FILE = Path("follow_state.json")
SLEEP_BETWEEN = 5  # seconds between requests

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return { "followed": []}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def make_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "auto-follow-cli"
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

def follow_user(headers, username_to_follow):
    url = f"{GITHUB_API}/user/following/{username_to_follow}"
    resp = requests.put(url, headers=headers)
    if resp.status_code == 204:
        print(f"[OK] Followed: {username_to_follow}")
        return True
    else:
        print(f"[ERROR] Failed to follow {username_to_follow}: {resp.status_code}")
        return False

def follow_back_new(token, username):
    headers = make_headers(token)
    state = load_state()
    already_followed = set(state.get("followed", []))

    print("Fetching your followers...")
    followers = get_all_followers(headers, username)
    print(f"Followers: {len(followers)}")

    print("Fetching who you already follow...")
    following = get_following(headers, username)
    print(f"Following: {len(following)}")

    to_follow = [u for u in followers if u not in following and u not in already_followed]
    print(f"New users to follow back: {len(to_follow)}")

    for user in to_follow:
        if follow_user(headers, user):
            already_followed.add(user)
        time.sleep(SLEEP_BETWEEN)

    state["followed"] = sorted(list(already_followed))
    save_state(state)
    print("Done.")