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

        table = self.table(self)
        self.cage = table.cage
        self.pagination = table.pagination

        while True:
            self.current_position, self.current_page, action = self.get_user_movement()

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
        current_page = self.current_page
        action = False

        mv = {Key.down: (1, 0), Key.up: (-1, 0), Key.right: (0, 1), Key.left: (0, -1)}

        user_input = self.get_user_input()

        if user_input == Key.enter:
            _ = input()
            action = True

        elif user_input in mv.keys():
            delta = mv[user_input]
            new_p = [c1 + c2 for c1, c2 in zip(self.current_position, delta)]
            if self.pagination and any([new_p in v for v in self.pagination.values()]):
                dir_ = [key for key, value in self.pagination.items() if new_p in value]
                assert len(dir_) == 1, "It goes in both directions!"
                # TODO должна сохранятся та же позиция, только в колонке 0
                # TODO движение назад
                # TODO нельзя выйти за рамки вперед
                # TODO нельзя выйти за рамки назад
                position = [0, 0]
                current_page += dir_[0]

            else:
                position = new_p if new_p in self.cage else position

        return position, current_page, action

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
