from Code.constants import SCREEN_WIDTH
from Code.functions.general import get_rows
from Code.tables.TableV2 import TableV2


class TagsTableV2(TableV2):
    def __init__(self, main):
        super(TagsTableV2, self).__init__(
            table_title="Games in Steam by tags",
            table_title_top_border="=",
            rows=get_rows(main),
            rows_top_border="=",
            rows_bottom_border="=",
            rows_centered=True,
            table_width=SCREEN_WIDTH,
            highlight=main.current_position,
        )
