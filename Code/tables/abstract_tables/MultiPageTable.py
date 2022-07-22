from math import ceil

from Code.functions.general import get_rows
from Code.tables.abstract_tables.SinglePageTable import SinglePageTable


class MultiPageTable(SinglePageTable):
    def __init__(self, main, max_rows, max_columns, items, title):

        self.max_rows = max_rows
        self.max_columns = max_columns
        self.max_page = ceil(len(items) / (self.max_rows * self.max_columns))
        self.total_on_page = self.max_rows * self.max_columns

        if main.current_page > self.max_page:
            main.current_page = self.max_page
            main.current_position[-1] = self.max_columns - 1

        elif main.current_page < 1:
            main.current_page = 1
            main.current_position[-1] = 0

        x, y = main.current_position

        self.current_page = main.current_page
        rows = get_rows(self, items)

        going_forward = main.page_delta == 1 and y == self.max_columns
        going_backward = main.page_delta == -1 and y < 0
        is_in_available_rows = x <= (len(rows) - 1)

        if going_forward and is_in_available_rows:
            main.current_position = [x, 0]

        elif going_forward and not is_in_available_rows:
            main.current_position = [len(rows) - 1, 0]

        elif going_backward:
            main.current_position = [x, self.max_columns - 1]

        elif not is_in_available_rows:
            main.current_position = [len(rows) - 1, y]

        # TODO ? дополнительные пробелы от стеночек зависят?
        shift = "  "
        arrow_l = "    " if main.current_page == 1 else "<<< "
        arrow_r = "    " if main.current_page == self.max_page else " >>>"
        super(MultiPageTable, self).__init__(
            title=f"{title}{shift}",
            rows=rows,
            current_position=main.current_position,
            footer=f"{arrow_l}[{main.current_page}/{self.max_page}]{arrow_r}{shift}",
            pagination=True,
        )
