import os

from Code.tables.CustomTable import CustomTable


class TagActionsTable(CustomTable):
    def __init__(self, tag, av_actions):
        os.system("cls")
        super(TagActionsTable, self).__init__(
            title=tag,
            rows=[e[0] for e in av_actions.values()],
        )
