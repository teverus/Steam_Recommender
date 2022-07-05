from Code.Action import Action
from Code.constants import SCREEN_WIDTH
from Code.functions.ui import get_user_choice
from Code.modules.BrowseGamesByTags import BrowseGamesByTags
from Code.modules.CheckNewGames import CheckNewGames
from Code.tables.Table import Table


class ApplicationImproved:
    def __init__(self):
        actions = {
            "1": Action(
                name="Add new games to database (if any)",
                function=CheckNewGames,
                break_after=True,
            ),
            "2": Action(
                name="Browse games by tags",
                function=BrowseGamesByTags,
                break_after=True,
            ),
        }

        table = Table(
            table_title="STEAM RECOMMENDER",
            table_title_border_top="=",
            rows=[action.name for action in actions.values()],
            rows_border_top="=",
            rows_border_bottom="=",
            table_width=SCREEN_WIDTH,
        )

        choice = get_user_choice(table.available_options)

        while True:
            action = actions[choice]

            action.function(action.arguments) if action.arguments else action.function()

            if action.break_after:
                break


if __name__ == "__main__":
    ApplicationImproved()
