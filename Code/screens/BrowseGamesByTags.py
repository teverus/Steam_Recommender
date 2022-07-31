from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.functions.general import get_tags
from Code.screens.PerformActionsWithATag import PerformActionsWithATag


class BrowseGamesByTags(Screen):
    def __init__(self):
        tags = get_tags()

        self.actions = [
            Action(
                name=tag,
                function=PerformActionsWithATag,
                arguments={"title": tag},
            )
            for tag in tags
        ]

        self.table = Table(
            title="Steam games by tags",
            rows=tags,
            max_rows=30,
            max_columns=3,
            footer_actions=[Action(name="Go back")],
        )

        super(BrowseGamesByTags, self).__init__()
