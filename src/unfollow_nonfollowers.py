import json
import time
from pathlib import Path
from utils import make_headers, get_all_followers, get_following
import requests

STATE_FILE = Path("unfollow_state.json")
SLEEP_BETWEEN = 5


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"unfollowed": []}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def unfollow_user(headers, username_to_unfollow):
    url = f"https://api.github.com/user/following/{username_to_unfollow}"
    resp = requests.delete(url, headers=headers)
    if resp.status_code == 204:
        print(f"[OK] Unfollowed: {username_to_unfollow}")
        return True
    else:
        print(f"[ERROR] Failed to unfollow {username_to_unfollow}: {resp.status_code}")
        return False


def unfollow_nonfollowers(token, username):
    headers = make_headers(token, agent="auto-unfollow-cli")
    state = load_state()
    already_unfollowed = set(state.get("unfollowed", []))

    print("Fetching your followers...")
    followers = get_all_followers(headers, username)
    print(f"Followers: {len(followers)}")

    print("Fetching who you follow...")
    following = get_following(headers, username)
    print(f"Following: {len(following)}")

    to_unfollow = [u for u in following if u not in followers and u not in already_unfollowed]
    print(f"Users who don’t follow you back: {len(to_unfollow)}")

    for user in to_unfollow:
        if unfollow_user(headers, user):
            already_unfollowed.add(user)
        time.sleep(SLEEP_BETWEEN)

    state["unfollowed"] = sorted(list(already_unfollowed))
    save_state(state)
    print("Done.")
