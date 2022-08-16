import webbrowser

from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth, APP_URL, HIDDEN, ID, GAMES, FAVORITE
from Code.functions.general import get_games, do_nothing, change_status, raise_an_error


class ShowGamesWithTag(Screen):
    def __init__(self, **kwargs):
        favorite = False if FAVORITE not in kwargs.keys() else kwargs[FAVORITE]
        hidden = False if HIDDEN not in kwargs.keys() else kwargs[HIDDEN]
        tag = kwargs["tag"]
        games = get_games(tag, favorite, hidden)

        # TODO !! Не показывать статус несовместимый с текущим
        self.actions = [
            [
                Action(
                    name=title,
                    function=self.open_game_in_steam,
                    arguments={"appid": appid},
                ),
                Action(
                    name="Make favorite",
                    function=self.change_game_status,
                    arguments={"appid": appid, "new_status": FAVORITE},
                ),
                Action(
                    name="Make hidden",
                    function=self.change_game_status,
                    arguments={"appid": appid, "new_status": HIDDEN},
                ),
            ]
            for title, appid in games.items()
        ]

        favorite_title = "favorite | " if favorite else ""
        hidden_title = "hidden | " if hidden else ""
        self.table = Table(
            title=f"{tag} | {favorite_title}{hidden_title}{len(games)} game(s)",
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

    def change_game_status(self, appid, new_status):
        change_status(ID, appid, new_status, GAMES, "game")

        actions = enumerate(self.actions)
        index = [i for i, action in actions if action[0].arguments["appid"] == appid]
        index = index[0] if len(index) == 1 else raise_an_error("Too many indices!")

        del self.actions[index]
        del self.table.rows_raw[index]
