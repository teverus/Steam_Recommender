from Code.constants import GAMES
from Code.functions.db import read_a_table
from string import ascii_lowercase as letters


def get_tags():
    # TODO получать теги из отдельной базы
    games = read_a_table(GAMES)
    known_tags = {}
    for index in range(len(games)):
        game_tags = games.loc[index].Tags.split(", ")
        for game_tag in game_tags:
            if game_tag:
                try:
                    known_tags[game_tag] += 1
                except KeyError:
                    known_tags[game_tag] = 1
    tags = sorted(list(known_tags.keys()))

    return tags


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
