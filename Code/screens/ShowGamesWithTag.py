import webbrowser

from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth, APP_URL, HIDDEN, ID, GAMES, FAVORITE
from Code.functions.general import (
    get_games,
    do_nothing,
    change_status,
    raise_an_error,
    get_new_table_title,
    change_entity_status,
)


class ShowGamesWithTag(Screen):
    def __init__(self, **kwargs):
        favorite = False if FAVORITE not in kwargs.keys() else kwargs[FAVORITE]
        hidden = False if HIDDEN not in kwargs.keys() else kwargs[HIDDEN]
        tag = kwargs["tag"]
        games = get_games(tag, favorite, hidden)

        self.actions = [
            [
                Action(
                    name=title,
                    function=self.open_game_in_steam,
                    arguments={"appid": appid},
                ),
                Action(
                    name="Unmake favorite" if favorite else "Make favorite",
                    function=self.change_game_status,
                    arguments={
                        "appid": appid,
                        "new_status": FAVORITE,
                        "favorite": favorite,
                        "hidden": hidden,
                    },
                ),
                Action(
                    name="Unmake hidden" if hidden else "Make hidden",
                    function=self.change_game_status,
                    arguments={
                        "appid": appid,
                        "new_status": HIDDEN,
                        "favorite": favorite,
                        "hidden": hidden,
                    },
                ),
            ]
            for title, appid in games.items()
        ]

        self.stub = [
            [
                Action(name="Nothing to show", function=do_nothing),
                Action(name="---", function=do_nothing),
                Action(name="---", function=do_nothing),
            ]
        ]

        self.actions = self.stub if not games else self.actions

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

    def change_game_status(self, appid, new_status, favorite, hidden):

        change_entity_status(
            self,
            new_status,
            favorite,
            hidden,
            x_column=ID,
            x_value=appid,
            table_name=GAMES,
            entity="game",
            main_index=0,
            attribute="arguments",
            sub_attribute="appid",
        )
