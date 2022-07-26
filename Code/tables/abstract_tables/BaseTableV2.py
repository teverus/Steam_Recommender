import os
from math import ceil

import bext
from pandas import DataFrame

from Code.constants import HIGHLIGHT, END_HIGHLIGHT


class BaseTableV2:
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
        pagination=None,
        max_rows=None,
        max_columns=1,
        current_page=1,
        # Footer
        footer=None,
        footer_centered=True,
        footer_bottom_border="=",
    ):
        # === General settings
        self.table_width = table_width
        self.highlight = highlight
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
        self.footer = self.get_footer()
        self.footer_bottom_border = footer_bottom_border
        self.footer_centered = footer_centered

        # Calculated values
        self.df = self.get_df()
        self.column_widths = self.get_column_widths()
        self.border_length = self.get_border_length()
        self.cage = self.get_cage()
        self.pagination = self.get_pagination(pagination)

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
            footer = footer.center if self.footer_centered else footer.ljust
            print(footer(self.border_length))
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

    def get_pagination(self, pagination):
        if pagination:
            go_next = [[row, self.max_columns] for row in range(self.max_rows)]
            go_prev = [[row, -1] for row in range(self.max_rows)]

            return {1: go_next, -1: go_prev}
        else:
            return False

    def print(self):
        self.print_table()

    def get_footer(self):
        if self.footer_raw:
            return self.footer_raw

        elif self.max_page:
            arrow_l = "    " if self.current_page == 1 else "<<< "
            arrow_r = "    " if self.current_page == self.max_page else " >>>"
            return f"{arrow_l}[{self.current_page}/{self.max_page}]{arrow_r}"

        else:
            return None

    def get_max_page(self):
        #  None if max_rows is None else self.get_max_page()
        if self.max_rows_raw is None:
            return None

        else:
            return ceil(len(self.rows_raw) / (self.max_rows * self.max_columns))

    def get_rows(self):
        if self.max_rows_raw:
            st = self.max_columns * (self.current_page - 1)
            rows = [
                list(row)
                for row in zip(
                    self.rows_raw[st * self.max_rows : (st + 1) * self.max_rows],
                    self.rows_raw[(st + 1) * self.max_rows : (st + 2) * self.max_rows],
                    self.rows_raw[(st + 2) * self.max_rows : (st + 3) * self.max_rows],
                )
            ]

            return rows

        else:
            return self.rows_raw

    def adjust_highlight_if_needed(self):
        x, y = self.highlight
        max_length = len(self.df) - 1

        highlight = [max_length, y] if x > max_length else [x, y]

        return highlight
