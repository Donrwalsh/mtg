import sys
from colorama import Fore


class Writer:

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
    def action_with_highlight(cls, message1, highlight, message2):
        sys.stdout.write(f"{Fore.BLUE}" + message1 +
                         f"{Fore.YELLOW}" + highlight +
                         f"{Fore.BLUE}" + message2 + "\n")

    @classmethod
    def pad_title(cls, title, length):
        result = title
        while len(result) < length:
            result += " "
        return result

    # @classmethod
    # def display_card(cls, card):
    #     sys.stdout.write(f"{Fore.WHITE}" + cls.pad_title("name", 12))
    #     sys.stdout.write(f"{Fore.YELLOW}" + cls.pad_title(card['name'], 33))
    #     sys.stdout.write(f"{Fore.WHITE}" + cls.pad_title("names", 12))
    #     sys.stdout.write(f"{Fore.YELLOW}" + cls.pad_title(card['names'], 33))