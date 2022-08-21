from Code.constants import SCREEN_WIDTH
from Code.BaseTable import BaseTable


# noinspection PyDefaultArgument
class Table(BaseTable):
    def __init__(
        self,
        title,
        rows,
        title_centered=True,
        rows_top_border="=",
        rows_bottom_border="=",
        rows_centered=True,
        highlight=[0, 0],
        max_rows=None,
        max_columns=None,
        column_widths=None,
        footer_actions=None,
    ):
        super(Table, self).__init__(
            # Table title
            table_title=title,
            table_title_top_border="=",
            table_title_centered=title_centered,
            # Rows
            rows=rows,
            rows_top_border=rows_top_border,
            rows_bottom_border=rows_bottom_border,
            rows_centered=rows_centered,
            # General table
            table_width=SCREEN_WIDTH,
            highlight=highlight,
            max_rows=max_rows,
            max_columns=max_columns,
            column_widths=column_widths,
            footer_actions=footer_actions,
        )
