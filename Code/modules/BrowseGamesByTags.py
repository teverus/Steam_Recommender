from math import ceil

from Code.Action import Action
from Code.Screen import Screen
from Code.functions.general import get_tags
from Code.modules.PerformActionsWithATag import PerformActionsWithATag
from Code.tables.TagsTable import TagsTable


class BrowseGamesByTags:
    def __init__(self):
        self.tags = get_tags()

        self.actions = [
            Action(
                name=tag,
                function=PerformActionsWithATag,
                arguments=tag,
                break_after=True,
            )
            for tag in self.tags
        ]

        # TODO footer
        self.table = TagsTable

        Screen(self)
