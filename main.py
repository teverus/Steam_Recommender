from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import TagStatus
from Code.screens.BrowseGamesByTags import BrowseGamesByTags
from Code.screens.CheckNewGames import CheckNewGames


class ApplicationV5(Screen):
    def __init__(self):
        self.actions = [
            Action(
                name="Check new games                             ",
                function=CheckNewGames,
            ),
            Action(
                name="Show tags ┌────────────────> without status ",
                function=BrowseGamesByTags,
            ),
            Action(
                name="          ├────────────────> favorite       ",
                function=BrowseGamesByTags,
                arguments={TagStatus.FAVORITE: True, "status_name": TagStatus.FAVORITE},
            ),
            Action(
                name="          └────────────────> hidden         ",
                function=BrowseGamesByTags,
                arguments={TagStatus.HIDDEN: True, "status_name": TagStatus.HIDDEN},
            ),
            Action(
                name="          ┌[Russian voice]─> without status ",
                function=BrowseGamesByTags,
                arguments={"russian_audio": True},
            ),
            Action(
                name="          ├[Russian voice]─> favorite       ",
                function=BrowseGamesByTags,
                arguments={
                    TagStatus.FAVORITE: True,
                    "status_name": TagStatus.FAVORITE,
                    "russian_audio": True,
                },
            ),
            Action(
                name="          └[Russian voice]─> hidden         ",
                function=BrowseGamesByTags,
                arguments={
                    TagStatus.HIDDEN: True,
                    "status_name": TagStatus.HIDDEN,
                    "russian_audio": True,
                },
            ),
        ]

        self.table = Table(
            title="Steam Recommender",
            rows=[action.name for action in self.actions],
        )

        super(ApplicationV5, self).__init__()


if __name__ == "__main__":
    ApplicationV5()
