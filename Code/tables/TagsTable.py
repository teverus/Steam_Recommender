from Code.functions.general import get_tags
from Code.tables.abstract_tables.MultiPageTable import MultiPageTable


class TagsTable(MultiPageTable):
    def __init__(self, main):
        super(TagsTable, self).__init__(
            title="Games in Steam by tags",
            items=get_tags(),
            max_rows=30,
            max_columns=3,
            main=main,
        )
