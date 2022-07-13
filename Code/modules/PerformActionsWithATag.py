from Code.tables.CustomTable import CustomTable


class PerformActionsWithATag:
    def __init__(self, tag_name):
        CustomTable(title=tag_name, rows=["Hello", "World"])
