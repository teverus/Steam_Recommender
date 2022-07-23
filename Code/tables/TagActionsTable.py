from Code.tables.abstract_tables.SinglePageTable import SinglePageTable


class TagActionsTable(SinglePageTable):
    def __init__(self, main):
        super(TagActionsTable, self).__init__(
            title=main.kwargs["title"],
            rows=[action.name for action in main.actions],
            current_position=main.current_position,
        )
