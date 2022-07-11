from Code.constants import SCREEN_WIDTH
from Code.tables.TableV2 import TableV2


class WelcomeTableV4(TableV2):
    def __init__(self, main):
        super(WelcomeTableV4, self).__init__(
            rows=[action.name for action in main.actions],
            rows_centered=True,
            rows_top_border="=",
            rows_bottom_border="=",
            table_title="Steam Recommender",
            table_title_top_border="=",
            table_width=SCREEN_WIDTH,
            highlight=main.current_position,
        )
