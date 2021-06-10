from colorama import Fore, init
from itertools import cycle

init(convert=True, autoreset=True)

color_list = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.RED,
    Fore.MAGENTA,
]
color_list = cycle(color_list)


def next_color():
    return next(color_list)


def rain(text):
    text = list(text)
    p = 0
    for index, i in enumerate(text):
        if i != " ":
            text[index] = f"{next_color()}{i}{Fore.RESET}"
        else:
            text[index] = text[index]
    final = "".join([str(elem) for elem in text])

    return final
