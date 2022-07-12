import bext
from pynput import keyboard
from pynput.keyboard import Key

from Code.Action import Action
from Code.modules.BrowseGamesByTags import BrowseGamesByTags
from Code.modules.CheckNewGames import CheckNewGames
from Code.tables.WelcomeTableV4 import WelcomeTableV4


class ApplicationV4:
    def __init__(self):
        bext.hide()
        self.pressed_key = None
        self.current_position = [0, 0]

        self.actions = [
            Action(
                name="Add new games to database (if any)",
                function=CheckNewGames,
            ),
            Action(
                name="Browse games by tags",
                function=BrowseGamesByTags,
                break_after=True,
            ),
        ]

        self.cage = WelcomeTableV4(self).cage

        while True:
            self.current_position, action = self.get_user_movement()

            if action:
                action = self.actions[self.current_position[0]]
                action()

                if action.break_after:
                    break

                print('\n Press "Enter" to continue...')
                self.wait_for_key(Key.enter)

            WelcomeTableV4(self)

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


if __name__ == "__main__":
    ApplicationV4()
