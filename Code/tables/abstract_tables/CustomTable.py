from Code.constants import SCREEN_WIDTH
from Code.tables.abstract_tables.BaseTableV2 import BaseTableV2


# noinspection PyDefaultArgument
class CustomTable(BaseTableV2):
    def __init__(
        self,
        title,
        rows,
        rows_bottom_border="=",
        rows_centered=True,
        current_position=[0, 0],
        footer=None,
        pagination=None,
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
            footer=footer,
            pagination=pagination,
        )
