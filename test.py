from Code.constants import SCREEN_WIDTH
from Code.tables.TableV2 import TableV2


class ApplicationTest:
    def __init__(self):
        TableV2(
            rows=[["Action 1", "badger"], ["Action 42", "pig"]],
            rows_centered=True,
            rows_top_border="=",
            rows_bottom_border="=",
            table_title="Table title",
            table_title_top_border="=",
            table_width=SCREEN_WIDTH,
            highlight=[0, 0],
        )


if __name__ == "__main__":
    ApplicationTest()
