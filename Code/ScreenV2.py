import bext
from pynput import keyboard
from pynput.keyboard import Key


class ScreenV2:
    def __init__(self):
        # Clear screen
        bext.hide()
        bext.clear()

        # Declare some variables that will be used later
        self.pressed_key = None
        self.current_page = 1

        # Print the table
        self.table.print()

        # Start infinite loop
        while True:

            # Get user input: action or movement
            self.table.highlight, self.page_delta, action = self.get_user_movement()

            # If an action is required, perform the action
            if action:
                x, y = self.table.highlight
                data_frame = self.table.df
                target_action_name = data_frame.iloc[x, y]
                action = [a for a in self.actions if a.name == target_action_name]
                assert len(action) == 1, "\n[ERROR] Found to many actions"
                action = action[0]
                action()

                # If the action starts a new screen, end this screen
                if action.break_after:
                    break

                print('\n Press "Enter" to continue...')
                self.wait_for_key(Key.enter)

            # Print the table with the new parameters
            self.table.print()

    def get_user_movement(self):
        # Declare three major variables that will be returned
        position = self.table.highlight
        page_delta = 0
        action = False

        # A set of coordinates
        mv = {Key.down: (1, 0), Key.up: (-1, 0), Key.right: (0, 1), Key.left: (0, -1)}

        # Get user input
        user_input = self.get_user_input()

        # If the user pressed "Enter"
        if user_input == Key.enter:
            _ = input()
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
                delta = [k for k, v in self.pagination.items() if newpos in v]
                assert len(delta) == 1, "Delta goes both directions!"
                delta = delta[0]
                position = newpos
                page_delta = delta
                self.current_page += page_delta

            # If not, replace the current position with the new position
            else:
                position = newpos if newpos in self.table.cage else position

        return position, page_delta, action

    def get_user_input(self):
        with keyboard.Listener(on_release=self.store_key) as listener:
            listener.join()

        return self.pressed_key

    def store_key(self, key):
        self.pressed_key = key
        return False

    def wait_for_key(self, target_key):
        user_input = self.get_user_input()
        while user_input != target_key:
            user_input = self.get_user_input()
