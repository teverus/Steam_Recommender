from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import TAGS, FAVORITE, HIDDEN, TAG
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
            # Action(
            #     name="Make this tag ┌─> favorite   ",
            #     function=change_status,
            #     arguments={
            #         "x_column": TAG,
            #         "x_value": kwargs["title"],
            #         "y_column": FAVORITE,
            #         "table_name": TAGS,
            #         "entity": "tag",
            #     },
            # ),
            # Action(
            #     name="              └─> hidden     ",
            #     function=change_status,
            #     arguments={
            #         "x_column": TAG,
            #         "x_value": kwargs["title"],
            #         "y_column": HIDDEN,
            #         "table_name": TAGS,
            #         "entity": "tag",
            #     },
            # ),
        ]

        self.table = Table(
            title=kwargs["title"],
            rows=[action.name for action in self.actions],
            footer_actions=[Action(name="Go back", function=do_nothing, go_back=True)],
        )

        self.kwargs = kwargs

        super(PerformActionsWithATag, self).__init__()
