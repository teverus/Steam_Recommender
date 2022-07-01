import os
from math import ceil

from Code.constants import SCREEN_WIDTH
from Code.tables.Table import Table


class TagsTable:
    def __init__(self, tags, current_page, max_rows=30, max_columns=3):
        milestone = max_columns * (current_page - 1)
        rows = [
            list(row)
            for row in zip(
                tags[milestone * max_rows: (milestone + 1) * max_rows],
                tags[(milestone + 1) * max_rows: (milestone + 2) * max_rows],
                tags[(milestone + 2) * max_rows: (milestone + 3) * max_rows],
            )
        ]

        os.system("cls")
        tags_table = Table(
            table_title="   Tags",
            table_title_border_top="=",
            rows=rows,
            rows_border_bottom="=",
            headers=["A", "B", "C"],
            headers_border_top="=",
            headers_centered=True,
            table_width=SCREEN_WIDTH,
        )

        columns = [e.strip().lower() for e in tags_table.headers[0].split("|")][1:]

        if current_page == 1:
            self.options = ["n"]
            go_to_previous_page = ""
        else:
            self.options = ["p", "n"]
            go_to_previous_page = ", p -> previous page"

        for column in columns:
            for available_option in tags_table.available_options:
                self.options.append(f"{available_option}{column}")

        max_columns = 3
        number_of_pages = ceil(len(tags) / (max_rows * max_columns))
        arrow_left = "   " if current_page == 1 else "<<<"
        arrow_right = ">>>"
        layout = f"   {arrow_left} {current_page}/{number_of_pages} {arrow_right}"
        print(f"{layout}".center(SCREEN_WIDTH))

        print(f"{'=' * SCREEN_WIDTH}")

        hints = f"  1a -> select a tag, n -> next page{go_to_previous_page}"
        print(hints.center(SCREEN_WIDTH))
