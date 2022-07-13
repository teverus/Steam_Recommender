import os

from Code.constants import SCREEN_WIDTH
from Code.functions.general import get_rows
from Code.tables.old.Table_Old1 import Table


class TagsTable_Old1:
    def __init__(self, main):
        os.system("cls")
        tags_table = Table(
            table_title="   Tags",
            table_title_border_top="=",
            rows=get_rows(main),
            rows_border_bottom="=",
            headers=["A", "B", "C"],
            headers_border_top="=",
            headers_centered=True,
            table_width=SCREEN_WIDTH,
        )

        self.adjust_options_and_hints(main)
        self.options = self.get_available_options(tags_table)
        self.print_arrows(main)

    def adjust_options_and_hints(self, main):
        if main.current_page == 1:
            self.options = ["n"]
            self.previous_page = ""
            self.next_page = ", n -> next page"
        elif main.current_page == main.max_page:
            self.options = ["p"]
            self.previous_page = ", p -> previous page"
            self.next_page = ""
        else:
            self.options = ["p", "n"]
            self.previous_page = ", p -> previous page"
            self.next_page = ", n -> next page"

    def get_available_options(self, tags_table):
        options = []

        columns = [e.strip().lower() for e in tags_table.headers[0].split("|")][1:]
        for column in columns:
            for available_option in tags_table.available_options:
                options.append(f"{available_option}{column}")

        return self.options + options

    def print_arrows(self, main):
        arrow_left = "   " if main.current_page == 1 else "<<<"
        arrow_right = "   " if main.current_page == main.max_page else ">>>"
        layout = f"   {arrow_left} {main.current_page}/{main.max_page} {arrow_right}"
        print(f"{layout}".center(SCREEN_WIDTH))

        print(f"{'=' * SCREEN_WIDTH}")

        hints = f"  1a -> select a tag{self.next_page}{self.previous_page}"
        print(hints.center(SCREEN_WIDTH))
