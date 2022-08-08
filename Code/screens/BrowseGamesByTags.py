from Code.Action import Action
from Code.Screen import Screen
from Code.Table import Table
from Code.functions.general import get_tags, do_nothing
from Code.screens.PerformActionsWithATag import PerformActionsWithATag


class BrowseGamesByTags(Screen):
    def __init__(
        self, favorite=False, hidden=False, russian_audio=False, status_name=""
    ):
        tags = get_tags(favorite=favorite, hidden=hidden, russian_audio=russian_audio)

        self.actions = [
            Action(name=tag, function=PerformActionsWithATag, arguments={"title": tag})
            for tag in tags
        ]

        name = f"{status_name} " if status_name else status_name
        self.table = Table(
            # TODO Обновлять значение после того, как поменял статус тегу
            title=f"Steam games by {name}tags / {len(tags)}",
            rows=tags,
            max_rows=30,
            max_columns=3,
            footer_actions=[Action(name="Go back", function=do_nothing, go_back=True)],
        )

        super(BrowseGamesByTags, self).__init__()
