from Code.Action import Action
from Code.Screen import Screen
from Code.modules.BrowseGamesByTags import BrowseGamesByTags
from Code.modules.CheckNewGames import CheckNewGames
from Code.tables.WelcomeTable import WelcomeTable


class ApplicationV4:
    def __init__(self):
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
        self.table = WelcomeTable
        Screen(self)


if __name__ == "__main__":
    ApplicationV4()
