from Code.constants import SCREEN_WIDTH
from Code.tables.Table import Table


class TagActionsTable(Table):
    def __init__(self, tag, av_actions):
        super(TagActionsTable, self).__init__(
            table_title=tag,
            rows=[e[0] for e in av_actions.values()],
            table_width=SCREEN_WIDTH,
            rows_border_top="=",
            rows_border_bottom="=",
            table_title_border_top="=",
            custom_index={"Go back": "00"},
        )
