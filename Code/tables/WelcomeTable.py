from Code.constants import SCREEN_WIDTH
from Code.tables.Table import Table


class WelcomeTable(Table):
    def __init__(self):
        super(WelcomeTable, self).__init__(
            table_title="Steam Recommender",
            table_title_border_top="=",
            rows=["Check new games in Steam", "Recommend games based on tags"],
            rows_border_top="=",
            rows_border_bottom="=",
            table_width=SCREEN_WIDTH,
        )
