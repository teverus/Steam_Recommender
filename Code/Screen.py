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

            # Check if there is an immediate action
            immediate_action = [a for a in self.actions if a.execute_instantly]

            if immediate_action:
                self.table.highlight, action = self.table.highlight, immediate_action[0]

            else:
                highlight, h_footer, action = self.get_user_action()
                self.table.highlight, self.table.highlight_footer = highlight, h_footer

            # If an action is required, perform the action
            if action:

                # Choose the right action
                if not immediate_action:
                    x, y = self.table.highlight
                    target_action_name = self.table.df.iloc[x, y]
                    if target_action_name:
                        act = [a for a in self.actions if a.name == target_action_name]
                        action = act[0] if len(act) == 1 else raise_an_error("Actions!")
                    else:
                        continue

                # Perform the action
                action()

                # If the action ends this screen, do it
                if action.go_back:
                    break

            # Print the table with the new parameters
            self.table.print()

    def get_user_action(self):
        # Declare major variables that will be returned
        highlight = self.table.highlight
        highlight_footer = self.table.highlight_footer
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
            new_pos = self.get_new_position(mv[user_input])

            # Check if the next/previous page was invoked
            page_change = self.get_page_change(new_pos)

            # Check if footer actions are involved
            footer_positions = self.get_footer_positions()

            # [1] Show next/previous page if the user moved to it
            if page_change:
                highlight = self.change_page(highlight, new_pos)

            # [2] Highlight footer if the user reaches the footer
            elif footer_positions and new_pos[0] in footer_positions:
                highlight = None
                highlight_footer = new_pos

            # [3] Do not move if the use tries to go below footer actions
            elif self.table.highlight_footer and new_pos[0] > max(footer_positions):
                pass

            # [4] Replace the current position with the new position if everything is OK
            elif new_pos in self.table.cage:
                highlight = new_pos
                highlight_footer = None if highlight_footer else highlight_footer

        return highlight, highlight_footer, action

    def get_page_change(self, newpos):
        try:
            page_change = any([newpos in v for v in self.table.pagination.values()])
        except AttributeError:
            page_change = None

        return page_change

    def get_footer_positions(self):
        footer_positions = False

        if self.table.footer_actions:
            t_len = len(self.table.df) - 1
            f_len = len(self.table.footer_actions)
            footer_positions = [t_len + num for num in range(1, f_len + 1)]

        return footer_positions

    def change_page(self, highlight, newpos):
        delta = [k for k, v in self.table.pagination.items() if newpos in v]
        assert len(delta) == 1, "Delta goes both directions!"
        delta = delta[0]

        go_below = self.table.current_page == 1 and delta == -1
        go_over = self.table.current_page == self.table.max_page and delta == 1
        within_boundaries = not go_below and not go_over

        x, y = highlight
        if within_boundaries and delta == 1:
            highlight = [x, 0]
            self.table.current_page += 1

        elif within_boundaries and delta == -1:
            highlight = [x, self.table.max_columns - 1]
            self.table.current_page -= 1

        return highlight

    def get_new_position(self, delta):
        move_within_footer = not self.table.highlight and self.table.highlight_footer
        highlight_footer = self.table.highlight_footer

        if move_within_footer and delta[1] != 0:
            new_position = self.table.highlight_footer

        elif move_within_footer and delta[0] != 0:
            new_position = [c1 + c2 for c1, c2 in zip(highlight_footer, delta)]

        else:
            new_position = [c1 + c2 for c1, c2 in zip(self.table.highlight, delta)]

        return new_position
