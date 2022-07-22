from Code.tables.abstract_tables.SinglePageTable import SinglePageTable


class PerformActionsWithATag:
    def __init__(self, tag_name):
        SinglePageTable(
            title=tag_name, rows=["Hello", "World"], current_position=[0, 0]
        )
