from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import TAGS, FAVORITE, HIDDEN, TAG, GO_BACK
from Code.functions.general import do_nothing, change_status
from Code.screens.ShowGamesWithTag import ShowGamesWithTag


class PerformActionsWithATag(Screen):
    def __init__(self, **kwargs):
        self.actions = [
            Action(
                name="Show games ┌─> without status",
                function=ShowGamesWithTag,
                arguments={"tag": kwargs["title"]},
            ),
            Action(
                name="           ├─> favorite      ",
                function=ShowGamesWithTag,
                arguments={"tag": kwargs["title"], FAVORITE: True},
            ),
            Action(
                name="           └─> hidden        ",
                function=ShowGamesWithTag,
                arguments={"tag": kwargs["title"], HIDDEN: True},
            ),
        ]

        self.table = Table(
            title=kwargs["title"],
            rows=[action.name for action in self.actions],
            footer_actions=[Action(name=GO_BACK, function=do_nothing, go_back=True)],
        )

        self.kwargs = kwargs

        super(PerformActionsWithATag, self).__init__()
