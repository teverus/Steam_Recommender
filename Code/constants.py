from colorama import Back, Fore

SCREEN_WIDTH = 107

ALL_GAMES = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?format=json"

FAVORITE = "Favorite"
HIDDEN = "Hidden"
TAGS = "Tags"
ID = "ID"

GAMES = "Games"
GAMES_COLUMNS = [ID, "Title", TAGS, "RussianAudio", FAVORITE, HIDDEN]

PROBLEMS = "Problems"
PROBLEMS_COLUMNS = [ID, "Problem"]

TAG = "Tag"
TAGS_COLUMNS = [TAG, "Number", FAVORITE, HIDDEN]

FILES = "Files"

STEAM_HOMEPAGE = "https://store.steampowered.com/"
APP_URL = "https://store.steampowered.com/app/"

HIGHLIGHT = Back.WHITE + Fore.BLACK
END_HIGHLIGHT = Back.BLACK + Fore.WHITE


class TagStatus:
    FAVORITE = "favorite"
    HIDDEN = "hidden"


class Key:
    DOWN = b"P"
    UP = b"H"
    RIGHT = b"M"
    LEFT = b"K"
    ENTER = b"\r"


class ColumnWidth:
    FULL = "Full"
    FIT = "Fit"
