from string import ascii_lowercase as letters

from pandas import DataFrame

from Code.constants import TAGS, TAGS_COLUMNS, FILES
from Code.functions.db import read_a_table, append_to_table


def get_tags():
    games = read_a_table(TAGS)
    return sorted(list(games.Tag))


def get_rows(self, tags):
    w = self.max_columns * (self.current_page - 1)
    rows = [
        list(row)
        for row in zip(
            tags[w * self.max_rows : (w + 1) * self.max_rows],
            tags[(w + 1) * self.max_rows : (w + 2) * self.max_rows],
            tags[(w + 2) * self.max_rows : (w + 3) * self.max_rows],
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
            append_to_table(df, TAGS, FILES)
