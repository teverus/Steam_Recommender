import json

from requests import get


def get_game_from_api(game_id):
    lang = "&l=english"
    url = f"https://store.steampowered.com/api/appdetails?appids={game_id}{lang}"
    return get(url)


def get_game_tags(game_id):
    response = get_game_in_steam(game_id)
    if "InitAppTagModal" in response.text:
        tags_script = (
            response.text.split("InitAppTagModal")[1].split("[")[1].split("]")[0]
        )
        tags_dict = json.loads(f"[{tags_script}]")
        tags = sorted([tag_info["name"] for tag_info in tags_dict])
        tags = ", ".join(tags)
    else:
        tags = ""

    return tags


def get_game_in_steam(game_id):
    url = f"https://store.steampowered.com/app/{game_id}/"
    return get(url)
