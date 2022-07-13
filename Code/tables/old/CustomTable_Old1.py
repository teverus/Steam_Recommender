from Code.constants import SCREEN_WIDTH
from Code.tables.old.Table_Old1 import Table


class CustomTable(Table):
    def __init__(self, title, actions):
        super(CustomTable, self).__init__(
            table_title=title,
            table_title_border_top="=",
            rows=[action.name for action in actions.values()],
            rows_border_top="=",
            rows_border_bottom="=",
            table_width=SCREEN_WIDTH,
        )
