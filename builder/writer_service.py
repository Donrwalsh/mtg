import sys
from colorama import Fore

import card_formatter


class Writer:

    # Fore.LIGHTRED_EX for errors
    # Fore.CYAN for informational notices only
    # Fore.BLUE for actions being taken
    # Fore.YELLOW for calling out individual items

    @classmethod
    def error(cls, message, error):
        sys.stdout.write(f"{Fore.LIGHTRED_EX}" + message + "\n" + str(error))

    @classmethod
    def error_card(cls, message, card):
        sys.stdout.write(f"{Fore.LIGHTRED_EX}" + message + "\n")
        # cls.display_card(card)
        print(card)

    @classmethod
    def action(cls, message):
        sys.stdout.write(f"{Fore.BLUE}" + message + "\n")

    @classmethod
    def note(cls, message):
        sys.stdout.write(f"{Fore.CYAN}" + message + "\n")

    @classmethod
    def note_stub(cls, message):
        sys.stdout.write(f"{Fore.CYAN}" + message)

    @classmethod
    def highlight_stub(cls, message):
        sys.stdout.write(f"{Fore.YELLOW}" + message)

    @classmethod
    def note_with_highlight(cls, message1, highlight, message2):
        sys.stdout.write(f"{Fore.CYAN}" + message1 +
                         f"{Fore.YELLOW}" + highlight +
                         f"{Fore.CYAN}" + message2 + "\n")

    @classmethod
    def action_with_highlight(cls, message1, highlight, message2):
        sys.stdout.write(f"{Fore.BLUE}" + message1 +
                         f"{Fore.YELLOW}" + highlight +
                         f"{Fore.BLUE}" + message2 + "\n")

    @classmethod
    def pad_right(cls, title, length):
        result = title
        while len(result) < length:
            result += " "
        return result

    @classmethod
    def pad_left(cls, msg, length):
        result = (length - len(msg)) * " "
        result += msg
        return result

    @classmethod
    def pad_both(cls, msg, length):
        pad = int((length - len(msg))/2)
        if pad + pad + len(msg) == length:
            result = " " * pad
        else:
            result = " " * (pad+1)
        result += msg
        result += " " * pad
        return result

    @classmethod
    def progress(cls, current, total):
        bars = int((current / total) * 10)
        return "[" + bars * "-" + (10 - bars) * " " + "]"

    @classmethod
    def display_card(cls, card, set):
        Formatter = card_formatter.CardFormatter(card)
        sys.stdout.write(f"{Fore.WHITE}" + cls.pad_right("name", 12))
        sys.stdout.write(f"{Fore.YELLOW}" + cls.pad_right(Formatter.name_for_console(), 33))
        if "names" in card:
            sys.stdout.write(f"{Fore.WHITE}" + cls.pad_right("names", 10))
            sys.stdout.write(f"{Fore.YELLOW}" + Formatter.names_for_console())
        sys.stdout.write('\n')
        sys.stdout.write(f"{Fore.WHITE}" + cls.pad_right("manaCost", 12))
        sys.stdout.write(f"{Fore.YELLOW}" + cls.pad_right(Formatter.mana_cost_for_console(), 33))
        sys.stdout.write(f"{Fore.WHITE}" + cls.pad_right("cmc", 6))
        sys.stdout.write(f"{Fore.YELLOW}" + cls.pad_right(Formatter.cmc_for_console(), 4))
        sys.stdout.write(f"{Fore.WHITE}" + cls.pad_right("set", 15))
        sys.stdout.write(f"{Fore.YELLOW}" + set + "\n")
        sys.stdout.write(f"{Fore.WHITE}" + cls.pad_right("colors", 12))
        sys.stdout.write(f"{Fore.YELLOW}" + cls.pad_right(Formatter.colors_for_console(), 43))
        sys.stdout.write(f"{Fore.WHITE}" + cls.pad_right("colorIdentity", 15))
        sys.stdout.write(f"{Fore.YELLOW}" + cls.pad_right(Formatter.color_identity_for_console(), 21) + "\n")

        card.pop('name', None)
        if "names" in card:
            card.pop('names', None)
        if "manaCost" in card:
            card.pop('manaCost', None)
        if "cmc" in card:
            card.pop('cmc', None)
        if "colors" in card:
            card.pop('colors', None)
        if "colorIdentity" in card:
            card.pop('colorIdentity', None)
        print(card)
