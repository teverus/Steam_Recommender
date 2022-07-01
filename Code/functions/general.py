from Code.constants import GAMES
from Code.functions.db import read_a_table


def get_tags():
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
