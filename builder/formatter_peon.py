

class FormatterPeon:

    def __init__(self, card):
        self.card = card

    def format_name(self):
        return "'" + self.card['name'].replace("'", "''") + "'"

    def format_names(self):
        if "names" in self.card:
            result = "'"
            i = 0
            for item in self.card['names']:
                i += 1
                result += item.replace("'", "''")
                if i < len(self.card['names']):
                    result += "//"
            result += "'"
            return result
        else:
            return self.format_name()

    def format_mana_cost(self):
        if "manaCost" in self.card:
            return "'" + self.card['manaCost'] + "'"
        else:
            return "null"

    def format_cmc(self):
        if "cmc" in self.card:
            return self.card["cmc"]
        else:
            return "null"