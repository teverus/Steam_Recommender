import bext
from colorama import Back, Fore
from pynput import keyboard
import colorama

colorama.init(autoreset=True)


def action(key):
    if key == keyboard.Key.down:
        bext.clear()
        bext.hide()
        print("Hello")
        print(Back.WHITE + Fore.BLACK + "World")
    elif key == keyboard.Key.up:
        bext.clear()
        bext.hide()
        print(Back.WHITE + Fore.BLACK + "Hello")
        print("World")
    return False


bext.clear()
bext.hide()
print(Back.WHITE + Fore.BLACK + "Hello")
print("World")

# Collect events until released
# with keyboard.Listener(on_release=action) as listener:
#     listener.join()

listener = keyboard.Listener(on_release=action)
listener.start()
aaa = listener
listener.join()

a = 1
