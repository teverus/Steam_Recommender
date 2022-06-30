from typing import List


def get_user_choice(
    available_options: List[str], prompt_message: str = "\n Please, enter your choice: "
) -> str:
    user_choice = input(prompt_message)

    while user_choice not in available_options:
        guidelines = ", ".join(available_options)
        print(f" [WARNING] You must enter one of these values: {guidelines}")
        user_choice = input("\n Please, enter your choice: ")

    return user_choice
