"""
TODO <<< не появляется на первой странице
TODO >>> не появляется на последней странице
"""

import os
from math import ceil

from Code.constants import GAMES, SCREEN_WIDTH
from Code.functions.db import read_a_table
from Code.functions.ui import get_user_choice
from Code.tables.Table import Table


class BrowseGamesByTags:
    def __init__(self):
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

        max_rows = 30
        max_columns = 3
        number_of_pages = ceil(len(tags) / (max_rows * max_columns))

        rows = [
            list(row)
            for row in zip(
                tags[:max_rows],
                tags[max_rows : max_rows * 2],
                tags[max_rows * 2 : max_rows * 3],
            )
        ]

        os.system("cls")
        tags_table = Table(
            table_title="Tags",
            table_title_border_top="=",
            rows=rows,
            rows_border_bottom="=",
            headers=["A", "B", "C"],
            headers_border_top="=",
            headers_centered=True,
            table_width=SCREEN_WIDTH,
        )

        columns = [e.strip().lower() for e in tags_table.headers[0].split("|")][1:]
        opts = []
        for column in columns:
            for available_option in tags_table.available_options:
                opts.append(f"{available_option}{column}")

        print(f"    1/{number_of_pages} >>>".center(SCREEN_WIDTH))
        print(f"{'=' * SCREEN_WIDTH}")

        instructions = (
            ' To select a tag, enter "1a", "2b"...\n'
            ' To go to the next page, enter "n"\n'
            ' To go to the previous page, enter "p"\n'
            " >>> "
        )
        choice = get_user_choice(opts, instructions)
        a = 1
