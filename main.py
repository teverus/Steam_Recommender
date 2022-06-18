from Code.Table import Table
from Code.constants import SCREEN_WIDTH


class Application:
    def __init__(self):
        Table(
            table_title="Steam Recommender",
            table_title_border_top="=",
            rows=["Check new games in Steam", "Recommend games based on tags"],
            rows_border_top="=",
            rows_border_bottom="=",
            table_width=SCREEN_WIDTH,
        )


if __name__ == "__main__":
    Application()
