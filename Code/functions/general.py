import msvcrt
import re
from math import ceil

from pandas import DataFrame

from Code.constants import (
    TAGS,
    TAGS_COLUMNS,
    FILES,
    Key,
    SCREEN_WIDTH,
    HIGHLIGHT,
    END_HIGHLIGHT,
    GAMES,
    FAVORITE,
    HIDDEN,
)
from Code.functions.db import read_a_table, append_to_table, update_a_table


def get_tags(favorite, hidden, russian_audio):
    tags = read_a_table(TAGS)

    fav_filter = "1" if favorite else "0"
    hid_filter = "1" if hidden else "0"

    tags = tags.loc[(tags.Favorite == fav_filter) & (tags.Hidden == hid_filter)]

    if russian_audio:
        tags = tags.loc[tags.RussianAudio == "1"]

    return sorted(tags.Tag)


def get_games(tag, favorite, hidden, russian):
    games = read_a_table(GAMES)

    fav_filter = "1" if favorite else "0"
    hid_filter = "1" if hidden else "0"
    rus_filter = "1" if russian else "0"

    games_with_tag = games.loc[
        (games.Tags.str.contains(tag))
        & (games.Favorite == fav_filter)
        & (games.Hidden == hid_filter)
        & (games.RussianAudio == rus_filter)
    ]
    games_with_tag = games_with_tag.sort_values(by="Title")
    titles = list(games_with_tag.Title)
    appids = list(games_with_tag.ID)
    games_with_tag = {k: v for k, v in zip(titles, appids)}

    dictionary = {replace_invalid_chars(k): v for k, v in games_with_tag.items()}

    return dictionary


def replace_invalid_chars(title):
    for special_char in ["®", "™"]:
        title = title.replace(special_char, "")

    for strange_char, proper_char in [("’", "'")]:
        title = title.replace(strange_char, proper_char)

    name = str(title.encode("utf-8"))
    # TODO Не убирать кириллицу 1990's -> 18 ????
    chars = re.findall(r"\\x\w{2}", name)
    if chars:
        for char in chars:
            name = name.replace(char, "?")

        length = len(chars)
        div = 0
        for number in range(2, 100):
            if length % number == 0:
                div = number
                break

        target = int(length / div)
        name = name.replace(f"{'?' * length}", f"{'?' * target}")

        title = name[2:-1]

    return title


def check_unique_tags(tags: str):
    known_tags = read_a_table(TAGS)
    known_tags = sorted(list(known_tags.Tag))

    possible_tags = tags.split(", ")
    for tag in possible_tags:
        if tag not in known_tags:
            df = DataFrame([], columns=TAGS_COLUMNS)
            df.loc[0] = [tag, 1, "0", "0", "0"]
            append_to_table(df, TAGS, FILES)


def do_nothing():
    pass


def raise_an_error(message):
    raise Exception(f"\n\n[ERROR] {message}")


def wait_for_key(target_key: Key):
    key = msvcrt.getch()
    while key != target_key:
        key = msvcrt.getch()


def show_message(message, border=" ", centered=True, upper=True):
    print(HIGHLIGHT)
    print(f"{border * SCREEN_WIDTH}")
    message = message.upper() if upper else message
    text = message.center if centered else message.ljust
    print(text(SCREEN_WIDTH))
    print(f"{border * SCREEN_WIDTH}{END_HIGHLIGHT}")


def change_status(x_column, x_value, y_column, y_value, table_name, entity):
    for status in [FAVORITE, HIDDEN]:
        new_value = y_value if status == y_column else 0
        update_a_table(x_column, x_value, status, new_value, table_name, FILES)

    un = "not " if y_value == 0 else ""
    show_message(f'The {entity} is now {un}{y_column}. Press "Enter" to continue...')

    wait_for_key(Key.ENTER)


def get_new_table_title(main, target_number):
    table_title = main.table.table_title

    current_number = table_title.split(" GAME(S)")[0].split(" ")[-1]

    return table_title.replace(f" {current_number} ", f" {target_number} ")


def get_new_tags_table_title(main, target_number):
    table_title = main.table.table_title

    current_number = table_title.split("[")[-1].split("]")[0]

    return table_title.replace(f"[{current_number}]", f"[{target_number}]")


def get_central_part(status_name, tags, russian_audio):
    name = f"{status_name} " if status_name else status_name
    rus_sound = "with Russian audio " if russian_audio else ""
    central = f"Steam games {rus_sound}by {name}tags [{len(tags)}]"
    expected_central_length = 45
    diff = expected_central_length - len(central)
    left_pad = f"{' ' * int((diff / 2))}"
    right_pad = left_pad
    if diff % 2 != 0:
        left_pad = f"{left_pad} "

    return f"{left_pad}{central}{right_pad}"


def change_entity_status(
    main,
    new_status,
    favorite,
    hidden,
    x_column,
    x_value,
    table_name,
    entity,
    main_column,
    attribute,
    sub_attribute=None,
):
    current_status = {FAVORITE: favorite, HIDDEN: hidden}
    value = 0 if current_status[new_status] else 1

    change_status(
        x_column=x_column,
        x_value=x_value,
        y_column=new_status,
        y_value=value,
        table_name=table_name,
        entity=entity,
    )

    index = get_index(main, main_column, x_value, attribute, sub_attribute)

    del main.actions[index]
    del main.table.rows_raw[index]

    main.table.highlight = [main.table.highlight[0], main_column]

    target_number = len(main.actions)

    if not main.actions:
        main.actions = main.stub
        main.table.rows_raw = [[sub_a.name for sub_a in a] for a in main.actions]
        target_number = 0
        main.table.highlight = None
        main.table.highlight_footer = [1, 0]

    main.table.table_title = get_new_tags_table_title(main, target_number)

    if ceil(len(main.actions) / main.table.max_rows) != main.table.max_page:
        main.table.max_page -= 1

        if main.table.current_page != 1:
            main.table.current_page -= 1


def get_index(main, main_index, x_value, attribute, sub_attribute):
    index = [
        i
        for i, action in enumerate(main.actions)
        if action[main_index].__getattribute__(attribute) == x_value
    ]
    if sub_attribute:
        index = [
            i
            for i, action in enumerate(main.actions)
            if action[main_index].__getattribute__(attribute)[sub_attribute] == x_value
        ]

    return index[0] if len(index) == 1 else raise_an_error("Too many indices!")
