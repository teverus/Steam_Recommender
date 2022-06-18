from Code.functions.ui import get_user_choice
from Code.modules.CheckNewGames import CheckNewGames
from Code.modules.RecommendGames import RecommendGames
from Code.tables.WelcomeTable import WelcomeTable


class Application:
    def __init__(self):
        self.options = {"1": CheckNewGames, "2": RecommendGames}

        available_options = WelcomeTable().available_options
        choice = get_user_choice(available_options)

        self.options[choice]()


if __name__ == "__main__":
    Application()
