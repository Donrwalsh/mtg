import sys
from colorama import Fore


class Writer:

    @classmethod
    def error(cls, message, error):
        sys.stdout.write(f"{Fore.LIGHTRED_EX}" + message + "\n" + str(error))

    @classmethod
    def action(cls, message):
        sys.stdout.write(f"{Fore.BLUE}" + message + "\n")

    @classmethod
    def action_with_highlight(cls, message1, highlight, message2):
        sys.stdout.write(f"{Fore.BLUE}" + message1 +
                         f"{Fore.YELLOW}" + highlight +
                         f"{Fore.BLUE}" + message2 + "\n")
