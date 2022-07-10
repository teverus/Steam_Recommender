import bext
import colorama
from colorama import Back as bg
from colorama import Fore as fg
from pynput import keyboard
from pynput.keyboard import Key

from Code.constants import SCREEN_WIDTH
from Code.tables.Table import Table

colorama.init(autoreset=True)


class ApplicationV3:
    def __init__(self):
        bext.clear()
        bext.hide()
        self.pressed_key = None
        self.current_position = (0, 0)

        Table(
            table_title="Steam Recommender",
            rows=[["Action #1", "Action #1-1"], ["Action #2", "Action #2-1"]],
            rows_centered=True,
            table_width=SCREEN_WIDTH,
            show_index=False,
            highlight=self.current_position,
        )

        self.current_position = self.get_user_movement()

        bext.clear()
        Table(
            table_title="Steam Recommender",
            rows=[["Action #1", "Action #1-1"], ["Action #2", "Action #2-1"]],
            rows_centered=True,
            table_width=SCREEN_WIDTH,
            show_index=False,
            highlight=self.current_position,
        )

        a = 1

    def get_user_movement(self):
        user_input = self.get_user_input()
        key_to_delta = {Key.down: (1, 0)}
        delta = key_to_delta[user_input]
        new_position = [
            coordinate1 + coordinate2
            for coordinate1, coordinate2 in zip(self.current_position, delta)
        ]

        return tuple(new_position)

    def get_user_input(self):
        with keyboard.Listener(on_release=self.store_key) as listener:
            listener.join()

        return self.pressed_key

    def store_key(self, key):
        self.pressed_key = key
        return False


if __name__ == "__main__":
    ApplicationV3()
