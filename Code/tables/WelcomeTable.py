from Code.tables.CustomTable import CustomTable


class WelcomeTable(CustomTable):
    def __init__(self, main):
        super(WelcomeTable, self).__init__(
            title="Steam Recommender",
            rows=[action.name for action in main.actions],
            current_position=main.current_position,
        )
