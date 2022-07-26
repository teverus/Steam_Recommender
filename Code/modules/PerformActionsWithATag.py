from Code.Action import Action
from Code.Screen import Screen
from Code.functions.general import do_nothing
from Code.Table import Table


class PerformActionsWithATag(Screen):
    def __init__(self, **kwargs):
        self.actions = [
            Action(name="Show games with this tag"),
            Action(name="Make tag favorite"),
            Action(name="Make tag hidden"),
            Action(name="Go back", function=do_nothing),
        ]

        self.table = Table(
            title=kwargs["title"], rows=[action.name for action in self.actions]
        )

        self.kwargs = kwargs

        super(PerformActionsWithATag, self).__init__()
