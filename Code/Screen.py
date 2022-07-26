import msvcrt
import os

import bext

from Code.constants import Key
from Code.functions.general import raise_an_error


class Screen:
    def __init__(self):
        # Clear screen and hide the cursor
        os.system("cls")
        bext.hide()

        # Print the table
        self.table.print()

        # Start the infinite loop
        while True:

            # Get user action: action or movement
            self.table.highlight, action = self.get_user_action()

            # If an action is required, perform the action
            if action:
                x, y = self.table.highlight
                target_action_name = self.table.df.iloc[x, y]
                act = [a for a in self.actions if a.name == target_action_name]
                action = act[0] if len(act) == 1 else raise_an_error("Too many actions")
                action()

                # If the action starts a new screen, end this screen
                if action.break_after:
                    break

            # Print the table with the new parameters
            self.table.print()

    def get_user_action(self):
        # Declare three major variables that will be returned
        position = self.table.highlight
        action = False

        # A set of coordinates
        mv = {Key.DOWN: (1, 0), Key.UP: (-1, 0), Key.RIGHT: (0, 1), Key.LEFT: (0, -1)}

        # Get user input
        user_input = msvcrt.getch()

        # If the user pressed "Enter"
        if user_input == Key.ENTER:
            action = True

        # If the user pressed one of the arrow keys
        elif user_input in mv.keys():

            # Get the new position based on the user input
            delta = mv[user_input]
            newpos = [c1 + c2 for c1, c2 in zip(self.table.highlight, delta)]

            # Check if the next/previous page was invoked
            is_multipage_table = bool(self.table.pagination)
            try:
                page_change = any([newpos in v for v in self.table.pagination.values()])
            except AttributeError:
                page_change = None

            # Show next/previous page if the user moved to it
            if is_multipage_table and page_change:
                delta = [k for k, v in self.table.pagination.items() if newpos in v]
                assert len(delta) == 1, "Delta goes both directions!"
                delta = delta[0]

                go_below = self.table.current_page == 1 and delta == -1
                go_over = self.table.current_page == self.table.max_page and delta == 1
                within_boundaries = not go_below and not go_over

                x, y = position
                if within_boundaries and delta == 1:
                    position = [x, 0]
                    self.table.current_page += 1

                elif within_boundaries and delta == -1:
                    position = [x, self.table.max_columns - 1]
                    self.table.current_page -= 1

            # If not, replace the current position with the new position
            else:
                position = newpos if newpos in self.table.cage else position

        return position, action
