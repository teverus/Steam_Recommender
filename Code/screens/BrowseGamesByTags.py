from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.constants import ColumnWidth
from Code.functions.general import get_tags, do_nothing, get_central_part
from Code.screens.PerformActionsWithATag import PerformActionsWithATag


class BrowseGamesByTags(Screen):
    def __init__(
        self, favorite=False, hidden=False, russian_audio=False, status_name=""
    ):
        tags = get_tags(favorite, hidden, russian_audio)

        self.actions = [
            [
                Action(name="Make favorite", function=do_nothing),
                Action(name="Make hidden", function=do_nothing),
                Action(
                    name=tag, function=PerformActionsWithATag, arguments={"title": tag}
                ),
                Action(name="No status", function=do_nothing),
                Action(name="Favorite", function=do_nothing),
                Action(name="Hidden", function=do_nothing),
            ]
            for tag in tags
        ]
        title = get_central_part(status_name, tags)
        self.table = Table(
            title=f"    Actions with this tag    |{title}|    SHOW GAMES WITH THIS TAG",
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

        # TODO ! Обновлять заголовок после того, как тег поменял статус
        # TODO !! Ставить заглушку, если удалился последний тег
        # TODO !!! Изменять количество тегов
        # TODO !!! Подставить правильную функцию
