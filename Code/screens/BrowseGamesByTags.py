from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth, TAG, TAGS, FAVORITE, HIDDEN, GO_BACK
from Code.functions.general import (
    get_tags,
    do_nothing,
    get_central_part,
    change_entity_status,
)
from Code.screens.ShowGamesWithTag import ShowGamesWithTag


class BrowseGamesByTags(Screen):
    def __init__(
        self, favorite=False, hidden=False, russian_audio=False, status_name=""
    ):
        tags = get_tags(favorite, hidden, russian_audio)

        self.actions = [
            [
                Action(
                    name="Unmake favorite" if favorite else "Make favorite",
                    function=self.change_tag_status,
                    arguments={
                        "new_status": FAVORITE,
                        "favorite": favorite,
                        "hidden": hidden,
                    },
                ),
                Action(
                    name="Unmake hidden" if hidden else "Make hidden",
                    function=self.change_tag_status,
                    arguments={
                        "new_status": HIDDEN,
                        "favorite": favorite,
                        "hidden": hidden,
                    },
                ),
                Action(
                    name=tag,
                    function=do_nothing,
                ),
                Action(
                    name="No status",
                    function=self.show_games,
                    arguments={"rus_audio": russian_audio},
                ),
                Action(
                    name="Favorite",
                    function=self.show_games,
                    arguments={"favorite": True, "rus_audio": russian_audio},
                ),
                Action(
                    name="Hidden",
                    function=self.show_games,
                    arguments={"hidden": True, "rus_audio": russian_audio},
                ),
            ]
            for tag in tags
        ]

        self.stub = [
            [
                Action(name="     ---     ", function=do_nothing),
                Action(name="     ---     ", function=do_nothing),
                Action(name="Nothing to show", function=do_nothing),
                Action(name="   ---   ", function=do_nothing),
                Action(name="  ---  ", function=do_nothing),
                Action(name="  ---  ", function=do_nothing),
            ]
        ]

        self.actions = self.stub if not tags else self.actions

        title = get_central_part(status_name, tags, russian_audio)
        title = title[1:-1] if any([favorite, hidden]) else title
        p = "     " if any([favorite, hidden]) else "    "
        self.table = Table(
            title=f"{p}Actions with this tag{p}|{title}|    SHOW GAMES WITH THIS TAG",
            title_centered=False,
            rows=[[action.name for action in actions] for actions in self.actions],
            max_rows=30,
            column_widths={
                0: ColumnWidth.FIT,
                1: ColumnWidth.FIT,
                2: ColumnWidth.FULL,
                3: ColumnWidth.FIT,
                4: ColumnWidth.FIT,
                5: ColumnWidth.FIT,
            },
            highlight=[0, 2],
            footer_actions=[Action(name=GO_BACK, function=do_nothing, go_back=True)],
        )

        super(BrowseGamesByTags, self).__init__()

    def change_tag_status(self, new_status, favorite, hidden):
        tag_title = list(self.table.df[2])[self.table.highlight[0]]

        change_entity_status(
            self,
            new_status,
            favorite,
            hidden,
            x_column=TAG,
            x_value=tag_title,
            table_name=TAGS,
            entity="tag",
            main_column=2,
            attribute="name",
        )

    def show_games(self, favorite=False, hidden=False, rus_audio=False):
        tag_title = list(self.table.df[2])[self.table.highlight[0]]
        ShowGamesWithTag(
            tag=tag_title, Favorite=favorite, Hidden=hidden, Russian_audio=rus_audio
        )
