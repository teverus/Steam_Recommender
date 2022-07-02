"""
TODO можно двигаться назад по страницам
TODO нельзя уйти за последнюю страницу
"""
from math import ceil

from Code.functions.general import get_tags
from Code.functions.ui import get_user_choice
from Code.tables.TagsTable import TagsTable


class BrowseGamesByTags:
    def __init__(self):
        self.tags = get_tags()
        self.current_page = 1
        self.max_rows = 30
        self.max_columns = 3
        self.max_page = ceil(len(self.tags) / (self.max_rows * self.max_columns))

        opts = TagsTable(self).options
        choice = get_user_choice(opts, " >>> ")

        while True:

            if choice == "n":
                self.current_page += 1
                opts = TagsTable(self).options
            elif choice == "p":
                raise Exception("Not implemented yet")
            else:
                raise Exception("Not implemented yet")

            choice = get_user_choice(opts, " >>> ")
