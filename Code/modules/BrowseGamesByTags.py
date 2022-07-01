"""
TODO можно двигаться назад по страницам
TODO >>> не появляется на последней странице
TODO нельзя уйти за последнюю страницу
"""
from Code.functions.general import get_tags
from Code.functions.ui import get_user_choice
from Code.tables.TagsTable import TagsTable


class BrowseGamesByTags:
    def __init__(self):
        self.tags = get_tags()
        self.current_page = 1

        opts = TagsTable(self.tags, self.current_page).options
        choice = get_user_choice(opts, " >>> ")

        while True:
            if choice == "n":
                self.current_page += 1
                opts = TagsTable(self.tags, self.current_page).options
            elif choice == "p":
                raise Exception("Not implemented yet")
            else:
                raise Exception("Not implemented yet")
            choice = get_user_choice(opts, " >>> ")
