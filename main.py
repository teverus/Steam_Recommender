import os

from Code.functions.ui import get_user_choice
from Code.modules.CheckNewGames import CheckNewGames
from Code.modules.BrowseGamesByTags import BrowseGamesByTags
from Code.tables.WelcomeTable import WelcomeTable


class Application:
    def __init__(self):
        self.options = {"1": CheckNewGames, "2": BrowseGamesByTags}

        os.system("cls")
        choice = get_user_choice(WelcomeTable().available_options)

        self.options[choice]()


if __name__ == "__main__":
    Application()
