from math import ceil

from Code.functions.general import get_tags
from Code.functions.ui import get_user_choice
from Code.modules.PerformActionsWithATag import PerformActionsWithATag
from Code.tables.old.TagsTable_Old1 import TagsTable_Old1


class BrowseGamesByTags_Old1:
    def __init__(self):
        self.tags = get_tags()
        self.current_page = 1
        self.max_rows = 30
        self.max_columns = 3
        self.max_page = ceil(len(self.tags) / (self.max_rows * self.max_columns))
        self.total_on_page = self.max_rows * self.max_columns

        options = TagsTable_Old1(self).options
        self.choice = get_user_choice(options, " >>> ")

        while True:

            if self.choice == "n":
                self.current_page += 1
                self.choice = get_user_choice(TagsTable_Old1(self).options, " >>> ")

            elif self.choice == "p":
                self.current_page -= 1
                self.choice = get_user_choice(TagsTable_Old1(self).options, " >>> ")

            else:
                PerformActionsWithATag(self)
                break