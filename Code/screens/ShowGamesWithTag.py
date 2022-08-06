from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.functions.general import get_games, do_nothing


class ShowGamesWithTag(Screen):
    def __init__(self, **kwargs):
        tag = kwargs["tag"]
        games = get_games(tag)

        self.actions = [Action(name=game) for game in games]

        self.table = Table(
            title=tag,
            rows=games,
            max_rows=30,
            max_columns=2,
            footer_actions=[Action(name="Go back", function=do_nothing, go_back=True)],
        )

        self.kwargs = kwargs

        super(ShowGamesWithTag, self).__init__()
