import json
import time
from pathlib import Path
from utils import make_headers, get_all_followers, get_following
import requests

STATE_FILE = Path("follow_state.json")
SLEEP_BETWEEN = 5


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"followed": []}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def follow_user(headers, username_to_follow):
    url = f"https://api.github.com/user/following/{username_to_follow}"
    resp = requests.put(url, headers=headers)
    if resp.status_code == 204:
        print(f"[OK] Followed: {username_to_follow}")
        return True
    else:
        print(f"[ERROR] Failed to follow {username_to_follow}: {resp.status_code}")
        return False


def follow_back_new(token, username):
    headers = make_headers(token, agent="auto-follow-cli")
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
