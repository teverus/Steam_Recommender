import os
from math import ceil
from string import ascii_lowercase as letters

from Code.constants import SCREEN_WIDTH
from Code.functions.general import get_tags
from Code.functions.ui import get_user_choice
from Code.tables.Table import Table
from Code.tables.TagsTable import TagsTable


class BrowseGamesByTags:
    def __init__(self):
        self.tags = get_tags()
        self.current_page = 1
        self.max_rows = 30
        self.max_columns = 3
        self.max_page = ceil(len(self.tags) / (self.max_rows * self.max_columns))
        self.total_on_page = self.max_rows * self.max_columns

        choice = get_user_choice(TagsTable(self).options, " >>> ")

        while True:

            if choice == "n":
                self.current_page += 1
                choice = get_user_choice(TagsTable(self).options, " >>> ")
            elif choice == "p":
                self.current_page -= 1
                choice = get_user_choice(TagsTable(self).options, " >>> ")
            else:
                index = int(choice[:-1]) - 1
                letter = letters.index(choice[-1])
                column_modifier = self.max_rows * letter
                page_modifier = self.total_on_page * (self.current_page - 1)

                start = 0 + column_modifier + page_modifier
                finish = self.max_rows + column_modifier + page_modifier
                part_of_tags = self.tags[start:finish]
                tag = part_of_tags[index]

                os.system("cls")
                options = Table(
                    table_title=tag,
                    rows=[
                        "Browse games with this tag",
                        "Make this tag favorite",
                        "Make this tag hidden",
                        "Go back",
                    ],
                    table_width=SCREEN_WIDTH,
                    rows_border_top="=",
                    rows_border_bottom="=",
                    table_title_border_top="=",
                    custom_index={"Go back": "00"},
                ).available_options
                choice = get_user_choice(options, " >>> ")
                # TODO что делать с тегом?
