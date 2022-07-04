from Code.constants import TagStatus, FAVORITE, HIDDEN, TAGS, FILES
from Code.functions.db import update_a_table
from Code.functions.general import get_tag_name
from Code.functions.ui import get_user_choice
from Code.tables.TagActionsTable import TagActionsTable


class PerformActionsWithATag:
    def __init__(self, main):
        self.tag = get_tag_name(main)

        action = 1
        argument = 2
        av_actions = {
            # TODO сделать Browse games with this tag
            "1": ["Browse games with this tag", None],
            # TODO сделать Make this tag favorite
            "2": ["Make this tag favorite", self.make_tag, TagStatus.FAVORITE],
            # TODO сделать Make this tag hidden
            "3": ["Make this tag hidden", self.make_tag, TagStatus.HIDDEN],
            # TODO сделать Go back
            "00": ["Go back", None],
        }

        options = TagActionsTable(self.tag, av_actions).available_options
        main.choice = get_user_choice(options, " >>> ")

        if main.choice in ["1", "00"]:
            a = 1
        else:
            selection = av_actions[main.choice]
            selection[action](selection[argument])

        # TODO цикл

    def make_tag(self, target_status):
        target_column = FAVORITE if target_status == TagStatus.FAVORITE else HIDDEN
        update_a_table("Tag", self.tag, target_column, 1, TAGS, FILES)
