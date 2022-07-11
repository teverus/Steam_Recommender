from Code.constants import SCREEN_WIDTH
from Code.tables.Table import Table


class WelcomeTableV3(Table):
    def __init__(self, main):
        super(WelcomeTableV3, self).__init__(
            table_title="Steam Recommender",
            rows=[action.name for action in main.actions],
            rows_centered=True,
            table_width=SCREEN_WIDTH,
            show_index=False,
            highlight=main.current_position,
        )
