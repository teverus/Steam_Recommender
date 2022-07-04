from datetime import datetime as dt
import re
from time import sleep

import requests
from requests import get

from Code.constants import (
    ALL_GAMES,
    GAMES_COLUMNS,
    GAMES,
    APP_URL,
    PROBLEMS,
)
from Code.functions.db import (
    append_row_to_table,
    read_a_table,
    record_an_error,
)
from Code.functions.general import check_unique_tags
from Code.functions.web import get_game_from_api, get_game_tags, get_game_in_steam


class CheckNewGames:
    def __init__(self):

        all_games = set(read_a_table(GAMES).ID).union(set(read_a_table(PROBLEMS).ID))
        new_games = set([e["appid"] for e in get(ALL_GAMES).json()["applist"]["apps"]])

        if all_games != new_games:
            diff = new_games - all_games

            time_start = dt.now()
            for index, appid in enumerate(diff):

                # Current state indication
                sleep(0.25)
                time_now = str(dt.now() - time_start).split(".")[0]
                print(
                    f" {index+1}/{len(diff)} | {time_now} | Appid: {str(appid).ljust(7)} | ",
                    end=""
                )

                # Connection Error
                try:
                    game = get_game_in_steam(appid)
                except requests.exceptions.ConnectionError:
                    print("Connection Error")
                    record_an_error([appid, "Connection Error"])
                    continue
                except requests.exceptions.TooManyRedirects:
                    print("Too many redirects")
                    record_an_error([appid, "Too many redirects"])
                    continue

                # Game page wasn't opened
                if APP_URL not in game.url:
                    print("Couldn't open in Steam")
                    record_an_error([appid, "Couldn't open in Steam"])
                    continue

                # AppId redirects to another Appid
                if f"/{appid}/" not in game.url:
                    old_id = appid
                    potential_appid = re.findall(r"app\/\d+", game.url)
                    assert len(potential_appid) == 1, "[ERROR] Couldn't parse new appid"
                    appid = int(potential_appid[0].strip("app/"))
                    record_an_error([old_id, f"Redirects to {appid}"])

                # Game info from SteamAPI
                try:
                    response = get_game_from_api(appid)
                except requests.exceptions.HTTPError:
                    print("HTTPError. Trying again...")
                    sleep(4)
                    response = get_game_from_api(appid)
                response.raise_for_status()
                try:
                    game_info = response.json()[str(appid)]
                except requests.exceptions.JSONDecodeError:
                    print("Couldn't decode JSON")
                    record_an_error([appid, "Couldn't decode JSON"])
                    continue

                if game_info["success"] and game_info["data"]["type"] == "game":
                    try:
                        english = "English" in game_info["data"]["supported_languages"]
                    except KeyError:
                        print("No languages mentioned")
                        record_an_error([appid, "No languages mentioned"])
                        continue

                    if not english:
                        print("No English")
                        record_an_error([appid, "No English"])
                        continue

                    game_data = game_info["data"]
                    name = game_data["name"]
                    tags = get_game_tags(appid)
                    russian_audio = "Russian<strong" in game_data["supported_languages"]

                    info = [appid, name, tags, russian_audio]
                    check_unique_tags(tags)
                    append_row_to_table(info, GAMES_COLUMNS, GAMES)
                    print("")

                else:
                    print("Not a game")
                    record_an_error([appid, "Not a game"])

        else:
            print(" No new games")
