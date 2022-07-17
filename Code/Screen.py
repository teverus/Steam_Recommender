import bext
from pynput import keyboard
from pynput.keyboard import Key


class Screen:
    def __init__(self, data):
        bext.hide()

        self.actions = data.actions
        self.table = data.table

        self.pressed_key = None
        self.current_position = [0, 0]
        self.current_page = 1
        self.page_delta = 0

        table = self.table(self)
        self.cage = table.cage
        self.pagination = table.pagination

        while True:
            self.current_position, self.page_delta, action = self.get_user_movement()

            if action:
                x, y = self.current_position
                table = self.table(self).df
                target_action_name = table.iloc[x, y]
                action = [a for a in self.actions if a.name == target_action_name]
                assert len(action) == 1, "\n[ERROR] Something is wrong with actions"
                action = action[0]
                action()

                if action.break_after:
                    break

                print('\n Press "Enter" to continue...')
                self.wait_for_key(Key.enter)

            self.table(self)

    def get_user_movement(self):
        position = self.current_position
        page_delta = 0
        action = False

        mv = {Key.down: (1, 0), Key.up: (-1, 0), Key.right: (0, 1), Key.left: (0, -1)}

        user_input = self.get_user_input()

        if user_input == Key.enter:
            _ = input()
            action = True
        elif user_input in mv.keys():
            delta = mv[user_input]
            newpos = [c1 + c2 for c1, c2 in zip(self.current_position, delta)]
            if self.pagination and any([newpos in v for v in self.pagination.values()]):
                delta = [k for k, v in self.pagination.items() if newpos in v]
                assert len(delta) == 1, "Delta goes both directions!"
                delta = delta[0]
                position = newpos
                page_delta = delta
                self.current_page += page_delta

            else:
                position = newpos if newpos in self.cage else position

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
