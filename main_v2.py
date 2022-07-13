# from Code.Action import Action
# from Code.functions.ui import get_user_choice
# from Code.modules.BrowseGamesByTags import BrowseGamesByTags
# from Code.modules.CheckNewGames import CheckNewGames
#
# # TODO Создать общий класс Screen
# # TODO Поменять на WelcomeScreen(Screen)
# from Code.tables.old.CustomTable_Old1 import CustomTable
#
#
# class ApplicationImproved:
#     def __init__(self):
#         actions = {
#             "1": Action(
#                 name="Add new games to database (if any)",
#                 function=CheckNewGames,
#                 break_after=True,
#             ),
#             "2": Action(
#                 name="Browse games by tags",
#                 function=BrowseGamesByTags,
#                 break_after=True,
#             ),
#         }
#
#         table = CustomTable(title="STEAM RECOMMENDER", actions=actions)
#
#         choice = get_user_choice(table.available_options)
#
#         while True:
#             action = actions[choice]
#
#             action.function(action.arguments) if action.arguments else action.function()
#
#             if action.break_after:
#                 break
#
#
# if __name__ == "__main__":
#     ApplicationImproved()
