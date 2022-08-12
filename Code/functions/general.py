import msvcrt
import re

from pandas import DataFrame

from Code.constants import (
    TAGS,
    TAGS_COLUMNS,
    FILES,
    Key,
    SCREEN_WIDTH,
    HIGHLIGHT,
    END_HIGHLIGHT,
    GAMES,
)
from Code.functions.db import read_a_table, append_to_table


def get_tags(favorite, hidden, russian_audio):
    tags = read_a_table(TAGS)

    fav_filter = "1" if favorite else ""
    hid_filter = "1" if hidden else ""

    tags = tags.loc[(tags.Favorite == fav_filter) & (tags.Hidden == hid_filter)]

    if russian_audio:
        tags = tags.loc[tags.RussianAudio == "1"]

    return sorted(tags.Tag)


def get_games(tag):
    games = read_a_table(GAMES)

    games_with_tag = games.loc[games.Tags.str.contains(tag)]
    games_with_tag = games_with_tag.sort_values(by="Title")
    titles = list(games_with_tag.Title)
    appids = list(games_with_tag.ID)
    games_with_tag = {k: v for k, v in zip(titles, appids)}

    dictionary = {replace_invalid_chars(k): v for k, v in games_with_tag.items()}

    return dictionary


def replace_invalid_chars(title):
    for special_char in ["®", "™"]:
        title = title.replace(special_char, "")

    for strange_char, proper_char in [("’", "'")]:
        title = title.replace(strange_char, proper_char)

    name = str(title.encode("utf-8"))
    # TODO ! Не убирать кириллицу 1990's -> 18 ????
    chars = re.findall(r"\\x\w{2}", name)
    if chars:
        for char in chars:
            name = name.replace(char, "?")

        length = len(chars)
        div = 0
        for number in range(2, 100):
            if length % number == 0:
                div = number
                break

        target = int(length / div)
        name = name.replace(f"{'?' * length}", f"{'?' * target}")

        title = name[2:-1]

    return title


def check_unique_tags(tags: str):
    known_tags = read_a_table(TAGS)
    known_tags = sorted(list(known_tags.Tag))

    possible_tags = tags.split(", ")
    for tag in possible_tags:
        if tag not in known_tags:
            df = DataFrame([], columns=TAGS_COLUMNS)
            df.loc[0] = [tag, 1, "", "", ""]
            append_to_table(df, TAGS, FILES)


def do_nothing():
    pass


def raise_an_error(message):
    raise Exception(f"\n [ERROR] {message}")


def wait_for_key(target_key: Key):
    key = msvcrt.getch()
    while key != target_key:
        key = msvcrt.getch()


def show_message(message, border=" ", centered=True):
    print(HIGHLIGHT)
    print(f"{border * SCREEN_WIDTH}")
    text = message.center if centered else message.ljust
    print(text(SCREEN_WIDTH))
    print(f"{border * SCREEN_WIDTH}")
    print(END_HIGHLIGHT)
