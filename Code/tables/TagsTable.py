from math import ceil

from Code.constants import SCREEN_WIDTH
from Code.functions.general import get_rows
from Code.tables.Table import Table


class TagsTable(Table):
    def __init__(self, main):
        tags = main.main.tags

        self.current_page = 1
        self.max_rows = 30
        self.max_columns = 3
        self.max_page = ceil(len(tags) / (self.max_rows * self.max_columns))
        self.total_on_page = self.max_rows * self.max_columns

        super(TagsTable, self).__init__(
            table_title="Games in Steam by tags",
            table_title_top_border="=",
            rows=get_rows(self, main),
            rows_top_border="=",
            rows_bottom_border="=",
            rows_centered=True,
            table_width=SCREEN_WIDTH,
            highlight=main.current_position,
            footer="<<< 1/5 >>>",
        )
