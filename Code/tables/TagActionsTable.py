import os

from Code.tables.abstract_tables.SinglePageTable import SinglePageTable


class TagActionsTable(SinglePageTable):
    def __init__(self, tag, av_actions):
        os.system("cls")
        super(TagActionsTable, self).__init__(
            title=tag,
            rows=[e[0] for e in av_actions.values()],
        )
