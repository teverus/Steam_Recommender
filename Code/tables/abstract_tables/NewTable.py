from Code.constants import SCREEN_WIDTH
from Code.tables.abstract_tables.BaseTableV2 import BaseTableV2


# noinspection PyDefaultArgument
class NewTable(BaseTableV2):
    def __init__(
        self,
        title,
        rows,
        rows_top_border="=",
        rows_bottom_border="=",
        rows_centered=True,
        highlight=[0, 0],
        max_rows=None,
        max_columns=1,
    ):
        super(NewTable, self).__init__(
            # Table title
            table_title=f"{title}",
            table_title_top_border="=",
            # Rows
            rows=rows,
            rows_top_border=rows_top_border,
            rows_bottom_border=rows_bottom_border,
            rows_centered=rows_centered,
            # General table
            pagination=True,
            table_width=SCREEN_WIDTH,
            highlight=highlight,
            max_rows=max_rows,
            max_columns=max_columns,
        )
