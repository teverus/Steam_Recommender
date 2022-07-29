from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import TAGS, FILES, Key
from Code.functions.db import update_a_table
from Code.functions.general import do_nothing, wait_for_key, show_message
from Code.screens.GamesWithTag import GamesWithTag


class PerformActionsWithATag(Screen):
    def __init__(self, **kwargs):
        self.actions = [
            Action(
                name="Show games              ",
                function=GamesWithTag,
                arguments={"tag": kwargs["title"]},
            ),
            Action(
                name="Make this tag | favorite",
                function=self.change_status,
                arguments={"status": "Favorite", "name": kwargs["title"]},
            ),
            Action(
                name="              | hidden  ",
                function=self.change_status,
                arguments={"status": "Hidden", "name": kwargs["title"]},
            ),
            Action(
                name="Go back                 ",
                function=do_nothing,
                go_back=True,
            ),
        ]

        self.table = Table(
            title=kwargs["title"], rows=[action.name for action in self.actions]
        )

        self.kwargs = kwargs

        super(PerformActionsWithATag, self).__init__()

    @staticmethod
    def change_status(status, name):

        update_a_table("Tag", name, status, 1, TAGS, FILES)

        show_message(f'The tag is now {status.lower()}. Press "Enter" to continue...')

        wait_for_key(Key.ENTER)
