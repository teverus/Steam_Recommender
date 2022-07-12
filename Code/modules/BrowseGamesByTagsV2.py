from math import ceil

from pynput import keyboard
from pynput.keyboard import Key

from Code.Action import Action
from Code.functions.general import get_tags
from Code.modules.PerformActionsWithATagV2 import PerformActionsWithATagV2
from Code.tables.TagsTableV2 import TagsTableV2


class BrowseGamesByTagsV2:
    def __init__(self):
        self.tags = get_tags()
        self.current_page = 1
        self.max_rows = 30
        self.max_columns = 3
        self.max_page = ceil(len(self.tags) / (self.max_rows * self.max_columns))
        self.total_on_page = self.max_rows * self.max_columns

        # --- Вынести в класс Screen ---------------------------------------------------

        self.pressed_key = None
        self.current_position = [0, 0]

        self.actions = [
            Action(
                function=PerformActionsWithATagV2,
                arguments=self.tags[0],
                break_after=True,
            )
        ]

        self.cage = TagsTableV2(self).cage

        while True:
            self.current_position, action = self.get_user_movement()

            if action:
                action = self.actions[self.current_position[0]]
                action()

                if action.break_after:
                    break

                print('\n Press "Enter" to continue...')
                self.wait_for_key(Key.enter)

            TagsTableV2(self)

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
