from string import ascii_lowercase as letters

from pandas import DataFrame

from Code.constants import TAGS, TAGS_COLUMNS
from Code.functions.db import read_a_table, append_to_table


def get_tags():
    games = read_a_table(TAGS)
    return sorted(list(games.Tag))


def get_rows(main):
    milestone = main.max_columns * (main.current_page - 1)
    rows = [
        list(row)
        for row in zip(
            main.tags[milestone * main.max_rows: (milestone + 1) * main.max_rows],
            main.tags[(milestone + 1) * main.max_rows: (milestone + 2) * main.max_rows],
            main.tags[(milestone + 2) * main.max_rows: (milestone + 3) * main.max_rows],
        )
    ]

    return rows


def get_tag_name(main):
    index = int(main.choice[:-1]) - 1
    letter = letters.index(main.choice[-1])
    column_modifier = main.max_rows * letter
    page_modifier = main.total_on_page * (main.current_page - 1)

    start = 0 + column_modifier + page_modifier
    finish = main.max_rows + column_modifier + page_modifier
    part_of_tags = main.tags[start:finish]
    tag = part_of_tags[index]

    return tag


def check_unique_tags(tags: str):
    known_tags = read_a_table(TAGS)
    known_tags = sorted(list(known_tags.Tag))

    possible_tags = tags.split(", ")
    for tag in possible_tags:
        if tag not in known_tags:
            df = DataFrame([], columns=TAGS_COLUMNS)
            df.loc[0] = [tag, 1]
            append_to_table(df, TAGS, "Files")
