import os
from math import ceil

import bext
from pandas import DataFrame

from Code.constants import HIGHLIGHT, END_HIGHLIGHT


class BaseTable:
    def __init__(
        self,
        # Rows
        rows,
        rows_top_border="-",
        rows_bottom_border="-",
        rows_centered=False,
        # Table title
        table_title="",
        table_title_centered=True,
        table_title_caps=True,
        table_title_top_border="-",
        # Table
        table_width=None,
        highlight=None,
        last_known_highlight=None,
        highlight_footer=None,
        current_page=1,
        max_rows=None,
        max_columns=1,
        # Footer
        footer=None,
        footer_centered=True,
        footer_bottom_border="=",
        footer_actions=None,
    ):
        # === General settings
        self.table_width = table_width
        self.highlight = highlight
        self.last_known_highlight = last_known_highlight
        self.highlight_footer = highlight_footer
        self.max_rows = max_rows if max_rows else len(rows)
        self.max_columns = max_columns
        self.current_page = current_page

        # === Table title
        self.table_title = table_title
        self.table_title_centered = table_title_centered
        self.table_title_caps = table_title_caps
        self.table_title_top_border = table_title_top_border

        # === Rows
        self.rows_raw = rows
        self.max_rows_raw = max_rows
        self.rows = self.get_rows()
        self.rows_top_border = rows_top_border
        self.rows_bottom_border = rows_bottom_border
        self.rows_centered = rows_centered

        # === Footer
        self.max_page = self.get_max_page()
        self.footer_raw = footer
        self.footer_actions = footer_actions
        self.footer = self.get_footer()
        self.footer_bottom_border = footer_bottom_border
        self.footer_centered = footer_centered

        # Calculated values
        self.df = self.get_df()
        self.column_widths = self.get_column_widths()
        self.border_length = self.get_border_length()
        self.cage = self.get_cage()
        self.pagination = self.get_pagination()

    def print_table(self):

        os.system("cls")
        bext.hide()

        # Table title top border
        if self.table_title and self.table_title_top_border:
            print(self.table_title_top_border * self.border_length)

        # Table title
        if self.table_title:
            centered = self.table_title_centered
            caps = self.table_title_caps
            self.table_title = self.table_title.upper() if caps else self.table_title
            tt = self.table_title.center if centered else self.table_title.ljust
            print(tt(self.border_length))

        # Rows top border
        if self.rows_top_border:
            print(self.rows_top_border * self.border_length)

        # Rows
        self.df = self.get_df()
        self.highlight = self.adjust_highlight_if_needed()
        for row in range(len(self.df)):
            a_row = []
            for column in range(self.max_columns):
                width = self.column_widths[column]
                data = self.df.iloc[row, column]
                data = data.center if self.rows_centered else data.ljust
                data = data(width, " ")
                if len(data) > width:
                    data = data[: -abs((len(data) - width) + 3)]
                    data = f"{data}..."
                highlighted = f"{HIGHLIGHT}{data}{END_HIGHLIGHT}"
                data = highlighted if [row, column] == self.highlight else data
                a_row.append(data)
            print(f" {' | '.join(a_row)} ")

        # Rows bottom border
        if self.rows_bottom_border:
            print(self.rows_bottom_border * self.border_length)

        # Footer
        if self.footer:
            footer = self.get_footer()

            for index, line in enumerate(footer):
                line = line.center if self.footer_centered else line.ljust
                line = line(self.border_length - 2)
                if self.highlight_footer:
                    highlighted = f"{HIGHLIGHT}{line}{END_HIGHLIGHT}"
                    is_highlighted = index == self.highlight_footer[0] - len(self.df)
                    line = highlighted if is_highlighted else line
                print(f" {line} ")

            print(self.footer_bottom_border * self.border_length)

        # Adjust the cage after the table has been recreated
        self.cage = self.get_cage()

    # ==================================================================================
    # === Helper class methods =========================================================
    # ==================================================================================

    def get_df(self):
        proper_rows = [r if isinstance(r, list) else [r] for r in self.get_rows()]
        max_columns = len(proper_rows[0])
        max_rows = len(proper_rows)

        df = DataFrame([], columns=[number for number in range(max_columns)])

        for row_index in range(max_rows):
            df.loc[row_index] = proper_rows[row_index]

        return df

    def get_column_widths(self):
        column_widths = {}

        for col in range(self.max_columns):

            if self.table_width:
                actual_width = self.table_width - (((self.max_columns - 1) * 3) + 2)
                diff = actual_width % self.max_columns
                if diff:
                    raise Exception(
                        f"Please, expand table_width by {self.max_columns - diff}"
                    )
                else:
                    per_col = int(actual_width / self.max_columns)
            else:
                per_col = max([len(self.df.iloc[r, col]) for r in range(self.max_rows)])

            column_widths[col] = per_col

        return column_widths

    def get_border_length(self):
        if self.table_width:
            return self.table_width
        else:
            return ((self.max_columns - 1) * 3) + 2 + sum(self.column_widths.values())

    def get_cage(self):
        x_axis = [number for number in range(len(self.df))]
        y_axis = [number for number in range(len(self.df.columns))]

        coordinates = []
        for x in x_axis:
            for y in y_axis:
                coordinates.append([x, y])

        return coordinates

    def get_pagination(self):
        go_next = [[row, self.max_columns] for row in range(self.max_rows)]
        go_prev = [[row, -1] for row in range(self.max_rows)]

        return {1: go_next, -1: go_prev}

    def print(self):
        self.print_table()

    def get_footer_pages(self):
        if self.max_page:
            arrow_l = "    " if self.current_page == 1 else "<<< "
            arrow_r = "    " if self.current_page == self.max_page else " >>>"

            return f"{arrow_l}[{self.current_page}/{self.max_page}]{arrow_r}"

        return None

    def get_footer(self):
        actions = [i.name for i in self.footer_actions] if self.footer_actions else None
        pages = self.get_footer_pages()

        if any([actions, pages]):
            actions = actions if actions is not None else []
            pages = [pages] if pages is not None else []

            return actions + pages

        return None

    def get_max_page(self):
        #  None if max_rows is None else self.get_max_page()
        if self.max_rows_raw is None:
            return None

        else:
            return ceil(len(self.rows_raw) / (self.max_rows * self.max_columns))

    def get_rows(self):
        if self.max_rows_raw:
            size = self.max_rows * self.max_columns
            previous_page = self.current_page - 1
            pack = self.rows_raw[size * previous_page : size * self.current_page]

            rows = []

            for col in range(self.max_columns):
                for row in range(self.max_rows):
                    if col == 0:
                        rows.append([pack[row]])
                    else:
                        try:
                            rows[row].append(pack[row + (self.max_rows * col)])
                        except IndexError:
                            rows[row].append("")

            return rows

        else:
            return self.rows_raw

    def adjust_highlight_if_needed(self):
        if self.highlight:
            x, y = self.highlight
            max_length = len(self.df) - 1

            highlight = [max_length, y] if x > max_length else [x, y]

            return highlight
