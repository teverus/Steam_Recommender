from math import ceil

from Code.Action import Action
from Code.Screen import Screen
from Code.functions.general import get_tags
from Code.modules.PerformActionsWithATag import PerformActionsWithATag
from Code.tables.TagsTable import TagsTable


class BrowseGamesByTags:
    def __init__(self):
        self.tags = get_tags()
        self.current_page = 1
        self.max_rows = 30
        self.max_columns = 3
        self.max_page = ceil(len(self.tags) / (self.max_rows * self.max_columns))
        self.total_on_page = self.max_rows * self.max_columns

        self.actions = [
            Action(
                function=PerformActionsWithATag,
                arguments=self.tags[0],
                break_after=True,
            )
        ]

        # TODO footer
        self.table = TagsTable

        Screen(self)
