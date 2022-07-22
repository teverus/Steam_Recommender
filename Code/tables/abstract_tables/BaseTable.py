import bext
import os

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
        pagination=None,
        # Footer
        footer=None,
        footer_centered=True,
    ):
        # === General settings
        self.table_width = table_width
        self.highlight = highlight

        # Declared in init
        self.number_of_cols = None
        self.number_of_rows = None

        # Calculated values
        self.df = self.get_df(rows)
        self.column_widths = self.get_column_widths()
        self.border_length = self.get_border_length()
        self.cage = self.get_cage()
        self.pagination = self.get_pagination(pagination)

        # === Table title
        self.table_title = table_title
        self.table_title_centered = table_title_centered
        self.table_title_caps = table_title_caps
        self.table_title_top_border = table_title_top_border

        # === Rows
        self.rows_top_border = rows_top_border
        self.rows_bottom_border = rows_bottom_border
        self.rows_centered = rows_centered

        # === Footer
        self.footer = footer
        self.footer_centered = footer_centered

        # === Print the table
        self.print_table()

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
        for row in range(self.number_of_rows):
            a_row = []
            for column in range(self.number_of_cols):
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
            footer = self.footer.center if self.footer_centered else self.footer.ljust
            print(footer(self.border_length))

    def get_df(self, rows):
        proper_rows = [r if isinstance(r, list) else [r] for r in rows]
        self.number_of_rows = len(proper_rows)
        self.number_of_cols = len(proper_rows[0])

        df = DataFrame([], columns=[number for number in range(self.number_of_cols)])
        for row_index in range(self.number_of_rows):
            df.loc[row_index] = proper_rows[row_index]

        return df

    def get_column_widths(self):
        column_widths = {}

        for col in range(self.number_of_cols):

            if self.table_width:
                actual_width = self.table_width - (((self.number_of_cols - 1) * 3) + 2)
                diff = actual_width % self.number_of_cols
                if diff:
                    raise Exception(
                        f"Please, expand table_width by {self.number_of_cols - diff}"
                    )
                else:
                    per_column = int(actual_width / self.number_of_cols)
            else:
                per_column = max(
                    [len(self.df.iloc[row, col]) for row in range(self.number_of_rows)]
                )

            column_widths[col] = per_column

        return column_widths

    def get_border_length(self):
        if self.table_width:
            return self.table_width
        else:
            return (
                ((self.number_of_cols - 1) * 3) + 2 + sum(self.column_widths.values())
            )

    def get_cage(self):
        x_axis = [number for number in range(self.number_of_rows)]
        y_axis = [number for number in range(self.number_of_cols)]

        coordinates = []
        for x in x_axis:
            for y in y_axis:
                coordinates.append([x, y])

        return coordinates

    def get_pagination(self, pagination):
        if pagination:
            go_next = [[row, self.number_of_cols] for row in range(self.number_of_rows)]
            go_prev = [[row, -1] for row in range(self.number_of_rows)]

            return {1: go_next, -1: go_prev}
        else:
            return False
