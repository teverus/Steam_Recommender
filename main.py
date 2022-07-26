from Code.Action import Action
from Code.Screen import Screen
from Code.modules.BrowseGamesByTags import BrowseGamesByTags
from Code.modules.CheckNewGames import CheckNewGames
from Code.Table import Table


class ApplicationV5(Screen):
    def __init__(self):
        self.actions = [
            Action(
                name="Add new games to database (if any)",
                function=CheckNewGames,
                break_after=False,
            ),
            Action(
                name="Browse games by tags",
                function=BrowseGamesByTags,
            ),
        ]

        self.table = Table(
            title="Steam Recommender",
            rows=[action.name for action in self.actions],
        )

        super(ApplicationV5, self).__init__()


if __name__ == "__main__":
    ApplicationV5()
