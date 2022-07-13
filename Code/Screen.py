import bext
from pynput import keyboard
from pynput.keyboard import Key


class Screen:
    def __init__(self, main):
        bext.hide()
        self.pressed_key = None
        self.current_position = [0, 0]
        self.main = main

        self.actions = main.actions

        self.cage = main.table(self).cage

        while True:
            self.current_position, action = self.get_user_movement()

            if action:
                action = self.actions[self.current_position[0]]
                action()

                if action.break_after:
                    break

                print('\n Press "Enter" to continue...')
                self.wait_for_key(Key.enter)

            main.table(self)

    def get_user_movement(self):
        position = self.current_position
        action = False

        mv = {Key.down: (1, 0), Key.up: (-1, 0), Key.right: (0, 1), Key.left: (0, -1)}

        user_input = self.get_user_input()

        if user_input == Key.enter:
            _ = input()
            action = True

        elif user_input in mv.keys():
            delta = mv[user_input]
            new_position = [c1 + c2 for c1, c2 in zip(self.current_position, delta)]
            position = new_position if new_position in self.cage else position

        return position, action

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
