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
            Action(name="Show common and favorite tags", function=BrowseGamesByTags),
            Action(name="Show favorite tags"),
            Action(name="Show hidden tags"),
            Action(name="[Russian voice] Show common and favorite tags"),
            Action(name="[Russian voice] Show favorite tags"),
            Action(name="[Russian voice] Show hidden tags"),
        ]

        self.table = Table(
            title="Steam Recommender",
            rows=[action.name for action in self.actions],
        )

        super(ApplicationV5, self).__init__()


if __name__ == "__main__":
    ApplicationV5()
