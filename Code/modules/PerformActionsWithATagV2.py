from Code.tables.CustomTableV2 import CustomTableV2


class PerformActionsWithATagV2:
    def __init__(self, tag_name):
        CustomTableV2(title=tag_name, rows=["Hello", "World"])
