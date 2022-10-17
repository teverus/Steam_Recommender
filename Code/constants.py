from colorama import Back, Fore

SCREEN_WIDTH = 117
CENTRAL_COLUMN_WIDTH = 55

ALL_GAMES = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?format=json"

FAVORITE = "Favorite"
HIDDEN = "Hidden"
TAGS = "Tags"
ID = "ID"
RUSSIAN_AUDIO = "Russian_audio"

GAMES = "Games"
GAMES_COLUMNS = [ID, "Title", TAGS, "RussianAudio", FAVORITE, HIDDEN]

PROBLEMS = "Problems"
PROBLEMS_COLUMNS = [ID, "Problem"]

TAG = "Tag"
TAGS_COLUMNS = [TAG, "Number", FAVORITE, HIDDEN, "RussianAudio"]

FILES = "Files"

STEAM_HOMEPAGE = "https://store.steampowered.com/"
APP_URL = "https://store.steampowered.com/app/"

HIGHLIGHT = Back.WHITE + Fore.BLACK
END_HIGHLIGHT = Back.BLACK + Fore.WHITE

GO_BACK = "[Q] Go back    "


class TagStatus:
    FAVORITE = "favorite"
    HIDDEN = "hidden"


class Key:
    DOWN = b"P"
    UP = b"H"
    RIGHT = b"M"
    LEFT = b"K"
    ENTER = b"\r"
    Q = b"q"
    Q_RU = b"\xa9"
    Z = b"z"
    Z_RU = b"\xef"
    X = b"x"
    X_RU = b"\xe7"


class ColumnWidth:
    FULL = "Full"
    FIT = "Fit"
