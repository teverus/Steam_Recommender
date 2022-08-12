from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth, APP_URL
from Code.functions.general import get_games, do_nothing

import webbrowser


class ShowGamesWithTag(Screen):
    def __init__(self, **kwargs):
        tag = kwargs["tag"]
        games = get_games(tag)

        self.actions = [
            [
                Action(
                    name=title,
                    function=self.open_game_in_steam,
                    arguments={"appid": appid},
                ),
                # TODO !!! Сделать Make favorite
                Action(name="Make favorite"),
                # TODO !!! Сделать Make hidden
                Action(name="Make hidden"),
            ]
            for title, appid in games.items()
        ]

        self.table = Table(
            title=f"{tag} | {len(games)} game(s)",
            rows=[[action.name for action in actions] for actions in self.actions],
            max_rows=30,
            column_widths={0: ColumnWidth.FULL, 1: ColumnWidth.FIT, 2: ColumnWidth.FIT},
            footer_actions=[Action(name="Go back", function=do_nothing, go_back=True)],
        )

        self.kwargs = kwargs

        super(ShowGamesWithTag, self).__init__()

    @staticmethod
    def open_game_in_steam(appid):
        webbrowser.open(f"{APP_URL}{appid}/")
        a = 1
