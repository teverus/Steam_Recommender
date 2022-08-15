import webbrowser

from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth, APP_URL, HIDDEN, ID, GAMES, FAVORITE
from Code.functions.general import get_games, do_nothing, change_status


class ShowGamesWithTag(Screen):
    def __init__(self, **kwargs):
        favorite = False if FAVORITE not in kwargs.keys() else kwargs[FAVORITE]
        hidden = False if HIDDEN not in kwargs.keys() else kwargs[HIDDEN]
        tag = kwargs["tag"]
        games = get_games(tag, favorite, hidden)

        # TODO !! Убирать игру из списка после того, как ей статус приделали
        self.actions = [
            [
                Action(
                    name=title,
                    function=self.open_game_in_steam,
                    arguments={"appid": appid},
                ),
                Action(
                    name="Make favorite",
                    function=change_status,
                    arguments={
                        "x_column": ID,
                        "x_value": appid,
                        "status": FAVORITE,
                        "table_name": GAMES,
                        "entity_type": "game",
                    },
                ),
                Action(
                    name="Make hidden",
                    function=change_status,
                    arguments={
                        "x_column": ID,
                        "x_value": appid,
                        "status": HIDDEN,
                        "table_name": GAMES,
                        "entity_type": "game",
                    },
                ),
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
