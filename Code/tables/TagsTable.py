from math import ceil

from Code.constants import SCREEN_WIDTH
from Code.functions.general import get_rows, get_tags
from Code.tables.Table import Table


class TagsTable(Table):
    def __init__(self, main):
        # TODO ! Вынести логику вот это
        tags = get_tags()

        self.current_page = main.current_page
        self.max_rows = 30
        self.max_columns = 3
        self.max_page = ceil(len(tags) / (self.max_rows * self.max_columns))
        self.total_on_page = self.max_rows * self.max_columns

        arrow_l = "    " if self.current_page == 1 else "<<< "
        arrow_r = "    " if self.current_page == self.max_page else " >>>"

        rows = get_rows(self, tags)

        x, y = main.current_position

        # TODO ! нельзя выйти за рамки вперед
        # TODO !! нельзя выйти за рамки назад

        going_forward = main.page_delta == 1 and y == self.max_columns
        going_backward = main.page_delta == -1 and y < 0
        is_in_expected_row_number = x <= (len(rows) - 1)

        if going_forward and is_in_expected_row_number:
            main.current_position = [x, 0]

        elif going_forward and not is_in_expected_row_number:
            main.current_position = [len(rows) - 1, 0]

        elif going_backward:
            main.current_position = [x, self.max_columns - 1]

        super(TagsTable, self).__init__(
            table_title="Games in Steam by tags  ",
            table_title_top_border="=",
            rows=rows,
            rows_top_border="=",
            rows_bottom_border="=",
            rows_centered=True,
            table_width=SCREEN_WIDTH,
            highlight=main.current_position,
            footer=f"{arrow_l}{self.current_page}/{self.max_page}{arrow_r}",
            pagination=True,
        )
