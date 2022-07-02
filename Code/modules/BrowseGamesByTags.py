"""
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

        choice = get_user_choice(TagsTable(self).options, " >>> ")

        while True:

            if choice == "n":
                self.current_page += 1
            elif choice == "p":
                self.current_page -= 1
            else:
                raise Exception("Not implemented yet")

            choice = get_user_choice(TagsTable(self).options, " >>> ")
