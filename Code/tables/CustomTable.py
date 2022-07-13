from Code.constants import SCREEN_WIDTH
from Code.tables.Table import Table


class CustomTable(Table):
    def __init__(
        self,
        title,
        rows,
        rows_bottom_border="=",
        rows_centered=True,
        current_position=None,
    ):
        super(CustomTable, self).__init__(
            table_title=title,
            table_title_top_border="=",
            rows=rows,
            rows_top_border="=",
            rows_bottom_border=rows_bottom_border,
            rows_centered=rows_centered,
            table_width=SCREEN_WIDTH,
            highlight=current_position,
        )
