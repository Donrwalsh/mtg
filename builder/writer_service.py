import sys
from colorama import Fore


class Writer:

    # Fore.LIGHTRED_EX for errors
    # Fore.CYAN for informational notices only
    # Fore.BLUE for actions being taken
    # Fore.YELLOW for calling out individual items

    @classmethod
    def SQL_error(cls, message, error, query):
        sys.stdout.write(f"{Fore.LIGHTRED_EX}" + message + "\n" + str(error) + "\n" + str(query))

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
    def action_stub(cls, message):
        sys.stdout.write(f"{Fore.BLUE}" + message)

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
    def action_with_highlight_stub(cls, message1, highlight, message2):
        sys.stdout.write(f"{Fore.BLUE}" + message1 +
                         f"{Fore.YELLOW}" + highlight +
                         f"{Fore.BLUE}" + message2)

    @classmethod
    def pad_right(cls, message, total_length):
        return message + " " * (total_length - len(message))

    @classmethod
    def progress(cls, current, total):
        bars = int((current / total) * 10)
        return "[" + bars * "-" + (10 - bars) * " " + "]"
