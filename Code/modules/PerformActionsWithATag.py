from Code.Action import Action
from Code.ScreenV2 import ScreenV2
from Code.functions.general import do_nothing
from Code.tables.abstract_tables.NewTable import NewTable


class PerformActionsWithATag(ScreenV2):
    def __init__(self, **kwargs):
        self.actions = [
            Action(name="Show games with this tag"),
            Action(name="Make tag favorite"),
            Action(name="Make tag hidden"),
            Action(name="Go back", function=do_nothing),
        ]

        self.table = NewTable(
            title=kwargs["title"], rows=[action.name for action in self.actions]
        )

        self.kwargs = kwargs

        super(PerformActionsWithATag, self).__init__()
