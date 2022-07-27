import msvcrt

from pandas import DataFrame

from Code.constants import (
    TAGS,
    TAGS_COLUMNS,
    FILES,
    Key,
    SCREEN_WIDTH,
    HIGHLIGHT,
    END_HIGHLIGHT,
)
from Code.functions.db import read_a_table, append_to_table


def get_tags():
    games = read_a_table(TAGS)
    return sorted(list(games.Tag))


def check_unique_tags(tags: str):
    known_tags = read_a_table(TAGS)
    known_tags = sorted(list(known_tags.Tag))

    possible_tags = tags.split(", ")
    for tag in possible_tags:
        if tag not in known_tags:
            df = DataFrame([], columns=TAGS_COLUMNS)
            df.loc[0] = [tag, 1, None, None]
            append_to_table(df, TAGS, FILES)


def do_nothing():
    pass


def raise_an_error(message):
    raise Exception(f"\n [ERROR] {message}")


def wait_for_key(target_key: Key):
    key = msvcrt.getch()
    while key != target_key:
        key = msvcrt.getch()


def show_message(message, border="-", centered=True):
    print(HIGHLIGHT)
    print(f"{border* SCREEN_WIDTH}")
    text = message.center if centered else message.ljust
    print(text(SCREEN_WIDTH))
    print(f"{border * SCREEN_WIDTH}")
    print(END_HIGHLIGHT)
