from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth, TAG, TAGS, FAVORITE, HIDDEN
from Code.functions.general import (
    get_tags,
    do_nothing,
    get_central_part,
    change_status,
    raise_an_error,
    get_new_tags_table_title,
)
from Code.screens.PerformActionsWithATag import PerformActionsWithATag
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
                    arguments={"new_status": FAVORITE},
                ),
                Action(
                    name="Unmake hidden" if hidden else "Make hidden",
                    function=self.change_tag_status,
                    arguments={"new_status": HIDDEN},
                ),
                Action(
                    name=tag,
                    function=do_nothing,
                ),
                Action(
                    name="No status",
                    function=self.show_games,
                ),
                Action(
                    name="Favorite",
                    function=self.show_games,
                    arguments={"favorite": True},
                ),
                Action(
                    name="Hidden",
                    function=self.show_games,
                    arguments={"hidden": True},
                ),
            ]
            for tag in tags
        ]

        title = get_central_part(status_name, tags)
        p = "     " if any([favorite, hidden]) else "    "
        title = title[1:-1] if any([favorite, hidden]) else title
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
            footer_actions=[Action(name="Go back", function=do_nothing, go_back=True)],
        )

        super(BrowseGamesByTags, self).__init__()

    def change_tag_status(self, new_status):
        tag_title = list(self.table.df[2])[self.table.highlight[0]]
        change_status(TAG, tag_title, new_status, TAGS, "tag")

        actions = enumerate(self.actions)
        index = [i for i, action in actions if action[2].name == tag_title]
        index = index[0] if len(index) == 1 else raise_an_error("Too many indices!")

        del self.actions[index]
        del self.table.rows_raw[index]

        target_number = len(self.actions)

        self.table.table_title = get_new_tags_table_title(self, target_number)

    def show_games(self, favorite=False, hidden=False):
        tag_title = list(self.table.df[2])[self.table.highlight[0]]
        ShowGamesWithTag(tag=tag_title, Favorite=favorite, Hidden=hidden)

        # TODO ! Ставить заглушку, если удалился последний тег
        # TODO !! Unmake favorite
        # TODO !! Unmake hidden
