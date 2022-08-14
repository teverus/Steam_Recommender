import webbrowser

from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth, APP_URL, HIDDEN, ID, GAMES, FAVORITE
from Code.functions.general import get_games, do_nothing, change_status


class ShowGamesWithTag(Screen):
    def __init__(self, **kwargs):
        tag = kwargs["tag"]
        games = get_games(tag)

        # TODO !!! Убирать игру из списка после того, как ей статус приделали
        # TODO ! Убрать несовместимый статус игры
        self.actions = [
            [
                Action(
                    name=title,
                    function=self.open_game_in_steam,
                    arguments={"appid": appid},
                ),
                Action(
                    name="Make favorite",
                    function=self.change_status,
                    arguments={"status": FAVORITE, "appid": appid},
                ),
                Action(
                    name="Make hidden",
                    function=self.change_status,
                    arguments={"status": HIDDEN, "appid": appid},
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

    @staticmethod
    def change_status(status, appid):
        change_status(ID, appid, status, GAMES, "game")
