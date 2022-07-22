from colorama import Back, Fore

SCREEN_WIDTH = 107

ALL_GAMES = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?format=json"

GAMES = "Games"
GAMES_COLUMNS = ["ID", "Title", "Tags", "RussianAudio"]

PROBLEMS = "Problems"
PROBLEMS_COLUMNS = ["ID", "Problem"]

TAGS = "Tags"
TAG = "Tag"
FAVORITE = "Favorite"
HIDDEN = "Hidden"
TAGS_COLUMNS = [TAG, "Number", FAVORITE, HIDDEN]

FILES = "Files"

STEAM_HOMEPAGE = "https://store.steampowered.com/"
APP_URL = "https://store.steampowered.com/app/"

HIGHLIGHT = Back.WHITE + Fore.BLACK
END_HIGHLIGHT = Back.BLACK + Fore.WHITE


class TagStatus:
    FAVORITE = "favorite"
    HIDDEN = "hidden"
