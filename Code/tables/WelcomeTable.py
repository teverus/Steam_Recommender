from Code.constants import SCREEN_WIDTH
from Code.tables.Table import Table


class WelcomeTable(Table):
    def __init__(self):
        super(WelcomeTable, self).__init__(
            table_title="Steam Recommender",
            table_title_border_top="=",
            rows=[
                "Add new games to database (if any)",
                "Browse games by tags",
                "Browse games by tags (+ Russian audio)",
                "Browse games by favorite tags",
                "Browse games by favorite tags (+ Russian audio)",
                "Browse games by hidden tags",
                "Browse games by hidden tags (+ Russian audio)",
                "Find games similar to a game"
            ],
            rows_border_top="=",
            rows_border_bottom="=",
            table_width=SCREEN_WIDTH,
        )
