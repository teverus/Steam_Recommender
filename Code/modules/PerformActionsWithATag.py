from Code.Action import Action
from Code.Screen import Screen
from Code.tables.TagActionsTable import TagActionsTable


class PerformActionsWithATag:
    def __init__(self, **kwargs):
        self.actions = [
            Action(name="Show games with this tag", break_after=True),
            Action(name="Make tag favorite", break_after=True),
            Action(name="Make tag hidden", break_after=True),
            Action(name="Go back", break_after=True),
        ]

        self.table = TagActionsTable
        self.kwargs = kwargs

        Screen(self)
