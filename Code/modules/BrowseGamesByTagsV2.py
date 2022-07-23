from Code.Action import Action
from Code.ScreenV2 import ScreenV2
from Code.functions.general import get_tags
from Code.modules.PerformActionsWithATag import PerformActionsWithATag
from Code.tables.abstract_tables.NewTable import NewTable


class BrowseGamesByTagsV2(ScreenV2):
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

        self.table = NewTable(
            title="Games in Steam by tags",
            rows=tags,
            max_rows=30,
            max_columns=3,
        )

        super(BrowseGamesByTagsV2, self).__init__()
