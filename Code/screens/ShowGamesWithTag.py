import webbrowser

from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth, APP_URL, Key, FILES, HIDDEN, ID, GAMES, FAVORITE
from Code.functions.db import update_a_table
from Code.functions.general import get_games, do_nothing, show_message, wait_for_key


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
        # TODO !! вынести
        update_a_table(ID, appid, status, 1, GAMES, FILES)

        show_message(f'The game is now {status.lower()}. Press "Enter" to continue...')

        wait_for_key(Key.ENTER)
