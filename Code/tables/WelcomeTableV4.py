from Code.tables.CustomTableV2 import CustomTableV2


class WelcomeTableV4(CustomTableV2):
    def __init__(self, main):
        super(WelcomeTableV4, self).__init__(
            title="Steam Recommender",
            rows=[action.name for action in main.actions],
            current_position=main.current_position,
        )
