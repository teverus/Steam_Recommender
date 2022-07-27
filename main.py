from Code.Action import Action
from Code.Screen import Screen
from Code.modules.BrowseGamesByTags import BrowseGamesByTags
from Code.modules.CheckNewGames import CheckNewGames
from Code.Table import Table


class ApplicationV5(Screen):
    def __init__(self):
        self.actions = [
            Action(
                name="Add games                                  ",
                function=CheckNewGames,
            ),
            Action(
                name="Show tags | without status |               ",
                function=BrowseGamesByTags,
            ),
            Action(
                name="          | without status | Russian voice ",
            ),
            Action(name="          | favorite       |               "),
            Action(name="          | favorite       | Russian voice "),
            Action(name="          | hidden         |               "),
            Action(name="          | hidden         | Russian voice "),
        ]

        self.table = Table(
            title="Steam Recommender",
            rows=[action.name for action in self.actions],
        )

        super(ApplicationV5, self).__init__()


if __name__ == "__main__":
    ApplicationV5()
