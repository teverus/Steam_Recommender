from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth
from Code.functions.general import get_games, do_nothing


class ShowGamesWithTag(Screen):
    def __init__(self, **kwargs):
        tag = kwargs["tag"]
        games = get_games(tag)

        self.actions = [
            [
                Action(name=game),
                Action(name="Make favorite"),
                Action(name="Make hidden"),
            ]
            for game in games
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
