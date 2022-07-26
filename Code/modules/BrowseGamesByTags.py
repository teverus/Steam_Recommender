# from math import ceil
#
# from Code.Action import Action
# from Code.Screen import Screen
# from Code.functions.general import get_tags
# from Code.modules.PerformActionsWithATag import PerformActionsWithATag
# from Code.tables.TagsTable import TagsTable
#
#
# class BrowseGamesByTags:
#     def __init__(self):
#         self.actions = [
#             Action(
#                 name=tag,
#                 function=PerformActionsWithATag,
#                 arguments={"title": tag},
#                 break_after=True,
#             )
#             for tag in get_tags()
#         ]
#
#         self.table = TagsTable
#
#         Screen(self)
