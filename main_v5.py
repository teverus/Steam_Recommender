from Code.Action import Action
from Code.ScreenV2 import ScreenV2
from Code.modules.BrowseGamesByTags import BrowseGamesByTags
from Code.modules.CheckNewGames import CheckNewGames
from Code.tables.TableOptions import TableOptions


class ApplicationV5(ScreenV2):
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

        self.table_options = TableOptions(
            title="Steam Recommender", rows=[action.name for action in self.actions]
        )

        super(ApplicationV5, self).__init__()


if __name__ == "__main__":
    ApplicationV5()
