
import json

def search_user(username):
    result = {}
    result[username] = []
    sources = {
        "github": get_github,
        "habr": get_habr,
        "tiktok": get_tiktok,
        "pikabu": get_pikabu,
        "reddit": get_reddit,
        "instagram": get_instagram
    }
    for source, func in sources.items():
        link = func(username)
        if link:
            result[username].append(link)
    with open("results.json", "w") as f:
        json.dump(result, f, indent=4)
