from Code.Action import Action
from Code.Screen import Screen
from Code.constants import FILES
from Code.functions.db import update_a_table
from Code.functions.general import do_nothing
from Code.Table import Table


class PerformActionsWithATag(Screen):
    def __init__(self, **kwargs):
        self.actions = [
            Action(name="Show games with this tag"),
            Action(
                name="Make tag favorite",
                function=update_a_table,
                arguments={
                    "row_name": "Tag",
                    "row_value": kwargs["title"],
                    "column_name": "Favorite",
                    "new_value": 1,
                    "table_name": "Tags",
                    "folder": FILES,
                },
            ),
            Action(name="Make tag hidden"),
            Action(name="Go back", function=do_nothing),
        ]

        self.table = Table(
            title=kwargs["title"], rows=[action.name for action in self.actions]
        )

        self.kwargs = kwargs

        super(PerformActionsWithATag, self).__init__()
