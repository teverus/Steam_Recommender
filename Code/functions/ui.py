from typing import List


def get_user_choice(available_options: List[str]) -> str:
    user_choice = input("\n Please, enter your choice: ")

    while user_choice not in available_options:
        guidelines = ", ".join(available_options)
        print(f" [WARNING] You must enter one of these values: {guidelines}")
        user_choice = input("\n Please, enter your choice: ")

    return user_choice
