from math import ceil

from Code.functions.general import get_rows, get_tags
from Code.tables.CustomTable import CustomTable


class TagsTable(CustomTable):
    def __init__(self, main):
        # TODO ! Сделать MultiPageTable
        tags = get_tags()

        self.max_rows = 30
        self.max_columns = 3
        self.max_page = ceil(len(tags) / (self.max_rows * self.max_columns))
        self.total_on_page = self.max_rows * self.max_columns

        if main.current_page > self.max_page:
            main.current_page = self.max_page
            main.current_position[-1] = self.max_columns - 1

        elif main.current_page < 1:
            main.current_page = 1
            main.current_position[-1] = 0

        x, y = main.current_position

        self.current_page = main.current_page

        arrow_l = "    " if main.current_page == 1 else "<<< "
        arrow_r = "    " if main.current_page == self.max_page else " >>>"

        rows = get_rows(self, tags)

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
        super(TagsTable, self).__init__(
            title=f"Games in Steam by tags{shift}",
            rows=rows,
            current_position=main.current_position,
            footer=f"{arrow_l}[{main.current_page}/{self.max_page}]{arrow_r}{shift}",
            pagination=True,
        )
