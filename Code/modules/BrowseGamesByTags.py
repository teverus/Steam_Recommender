from Code.Action import Action
from Code.ScreenV2 import ScreenV2
from Code.functions.general import get_tags
from Code.modules.PerformActionsWithATag import PerformActionsWithATag
from Code.tables.abstract_tables.NewTable import NewTable


class BrowseGamesByTags(ScreenV2):
    def __init__(self):
        tags = get_tags()

        self.actions = [
            Action(
                name=tag,
                function=PerformActionsWithATag,
                arguments={"title": tag},
                break_after=False,
            )
            for tag in tags
        ]

        self.table = NewTable(
            title="Steam games by tags",
            rows=tags,
            max_rows=30,
            max_columns=3,
        )

        super(BrowseGamesByTags, self).__init__()
