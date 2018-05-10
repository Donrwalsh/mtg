# from writer_service import Writer


class CardFormatter:

    def __init__(self, card):
        self.card = card
        self.db = {
            'name': self.name_for_db(),
            'names': self.names_for_db(),
            'manaCost': self.mana_cost_for_db(),
            'cmc': self.cmc_for_db(),
            'colors': self.colors_for_db(),
            'colorIdentity': self.color_identity_for_db(),
            'type': self.type_for_db(),
            'supertypes': self.supertypes_for_db()
        }
        self.console = {
            'name': self.name_for_console(),
            'names': self.names_for_console(),
            'manaCost': self.mana_cost_for_console(),
            'cmc': self.cmc_for_console(),
            'colors': self.colors_for_console(),
            'colorIdentity': self.color_identity_for_console(),
            'type': self.type_for_console(),
            'supertypes': self.supertypes_for_console()
        }

    def name_for_db(self):
        return "'" + self.card['name'].replace("'", "''") + "'"

    def name_for_console(self):
        return self.card['name']

    def names_for_db(self):
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
            return self.name_for_db()

    def names_for_console(self):
        if "names" in self.card:
            result = "['"
            for name in self.card['names']:
                result += name
                if self.card['names'].index(name) == len(self.card['names'])-1:
                    result += "']"
                else:
                    result += "', '"
            return result
        else:
            return ""

    def mana_cost_for_db(self):
        if "manaCost" in self.card:
            return "'" + self.card['manaCost'] + "'"
        else:
            return "null"

    def mana_cost_for_console(self):
        if "manaCost" in self.card:
            return self.card['manaCost']
        else:
            return "null"

    def cmc_for_db(self):
        if "cmc" in self.card:
            return str(self.card["cmc"])
        else:
            return "null"

    def cmc_for_console(self):
        if "cmc" in self.card:
            return str(self.card['cmc'])
        else:
            return "null"

    def colors_for_db(self):
        if "colors" in self.card:
            return self.translate_color(self.card['colors'])
        else:
            return "'Colorless'"

    def colors_for_console(self):
        result = ""
        if "colors" in self.card:
            for color in self.card['colors']:
                if self.card['colors'].index(color) == 0:
                    result += "['"
                result += color
                if self.card['colors'].index(color) == len(self.card['colors']) -1:
                    result += "']"
                else:
                    result += "', '"
        else:
            result = "['Colorless']"
        return result

    def color_identity_for_db(self):
        if "colorIdentity" in self.card:
            return self.translate_color(self.card['colorIdentity'])
        else:
            return "'Colorless'"

    def color_identity_for_console(self):
        result = ""
        if "colorIdentity" in self.card:
            for color_identity in self.card['colorIdentity']:
                if self.card['colorIdentity'].index(color_identity) == 0:
                    result += "['"
                result += color_identity
                if self.card['colorIdentity'].index(color_identity) == len(self.card['colorIdentity']) - 1:
                    result += "']"
                else:
                    result += "', '"
        else:
            result = "['C']"
        return result

    def type_for_db(self):
        return "'" + (self.card['type'].replace("’", "''")).replace("—", "-") + "'"

    def type_for_console(self):
        return self.card['type']

    def supertypes_for_console(self):
        result = ""
        if "supertypes" in self.card:
            for super_type in self.card['supertypes']:
                if self.card['supertypes'].index(super_type) == 0:
                    result += "['"
                result += super_type
                if self.card['supertypes'].index(super_type) == len(self.card['supertypes']) - 1:
                    result += "']"
                else:
                    result += "', '"
        else:
            result = "[]"
        return result

    def supertypes_for_db(self):
        result = "'"
        if "supertypes" in self.card:
            for super_type in self.card['supertypes']:
                result += super_type
                if self.card['supertypes'].index(super_type) != len(self.card['supertypes']) - 1:
                    result += ", "
                else:
                    result += "'"
            return result
        else:
            return "null"

    def translate_color(self, colorArray):
        if len(colorArray) == 1:
            if len(colorArray[0]) == 1:
                if colorArray == ['W']:
                    return "'White'"
                elif colorArray == ['U']:
                    return "'Blue'"
                elif colorArray == ['B']:
                    return "'Black'"
                elif colorArray == ['R']:
                    return "'Red'"
                elif colorArray == ['G']:
                    return "'Green'"
            else:
                return "'" + colorArray[0] + "'"
        elif len(colorArray) == 2:
            if colorArray == ['White', 'Blue'] or sorted(colorArray) == ['U', 'W']:
                return "'Azorius'"
            elif colorArray == ['Blue', 'Black'] or sorted(colorArray) == ['B', 'U']:
                return "'Dimir'"
            elif colorArray == ['Black', 'Red'] or sorted(colorArray) == ['B', 'R']:
                return "'Rakdos'"
            elif colorArray == ['Red', 'Green'] or sorted(colorArray) == ['G', 'R']:
                return "'Gruul'"
            elif colorArray == ['White', 'Green'] or sorted(colorArray) == ['G', 'W']:
                return "'Selesnya'"
            elif colorArray == ['White', 'Black'] or sorted(colorArray) == ['B', 'W']:
                return "'Orzhov'"
            elif colorArray == ['Blue', 'Red'] or sorted(colorArray) == ['R', 'U']:
                return "'Izzet'"
            elif colorArray == ['Black', 'Green'] or sorted(colorArray) == ['B', 'G']:
                return "'Golgari'"
            elif colorArray == ['White', 'Red'] or sorted(colorArray) == ['R', 'W']:
                return "'Boros'"
            elif colorArray == ['Blue', 'Green'] or sorted(colorArray) == ['G', 'U']:
                return "'Simic'"
            # else:
            #     Writer.error_card("Unable to format color on card:", self.card)
            #     exit()
        elif len(colorArray) == 3:
            if colorArray == ['White', 'Blue', 'Green'] or sorted(colorArray) == ['G', 'U', 'W']:
                return "'Bant'"
            elif colorArray == ['White', 'Blue', 'Black'] or sorted(colorArray) == ['B', 'U', 'W']:
                return "'Esper'"
            elif colorArray == ['Blue', 'Black', 'Red'] or sorted(colorArray) == ['B', 'R', 'U']:
                return "'Grixis'"
            elif colorArray == ['Black', 'Red', 'Green'] or sorted(colorArray) == ['B', 'G', 'R']:
                return "'Jund'"
            elif colorArray == ['White', 'Red', 'Green'] or sorted(colorArray) == ['G', 'R', 'W']:
                return "'Naya'"
            elif colorArray == ['White', 'Blue', 'Red'] or sorted(colorArray) == ['R', 'U', 'W']:
                return "'Jeskai'"
            elif colorArray == ['White', 'Black', 'Red'] or sorted(colorArray) == ['B', 'R', 'W']:
                return "'Mardu'"
            elif colorArray == ['Blue', 'Black', 'Green'] or sorted(colorArray) == ['B', 'G', 'U']:
                return "'Sultai'"
            elif colorArray == ['Blue', 'Red', 'Green'] or sorted(colorArray) == ['G', 'R', 'U']:
                return "'Temur'"
            elif colorArray == ['White', 'Black', 'Green'] or sorted(colorArray) == ['B', 'G', 'W']:
                return "'Abzan'"
            # else:
            #     Writer.error_card("Unable to format color on card:", self.card)
            #     exit()
        elif len(colorArray) == 4:
            if colorArray == ['Blue', 'Black', 'Red', 'Green'] or sorted(colorArray) == ['B', 'G', 'R', 'U']:
                return "'Glint-Eye'"
            elif colorArray == ['White', 'Black', 'Red', 'Green'] or sorted(colorArray) == ['B', 'G', 'R', 'W']:
                return "'Dune'"
            elif colorArray == ['White', 'Blue', 'Red', 'Green'] or sorted(colorArray) == ['G', 'R', 'U', 'W']:
                return "'Ink-Treader'"
            elif colorArray == ['White', 'Blue', 'Black', 'Green'] or sorted(colorArray) == ['B', 'G', 'U', 'W']:
                return "'Witch'"
            elif colorArray == ['White', 'Blue', 'Black', 'Red'] or sorted(colorArray) == ['B', 'R', 'U', 'W']:
                return "'Yore'"
            # else:
            #     Writer.error_card("Unable to format color on card:", self.card)
            #     exit()
        elif len(colorArray) == 5:
            return "'5Color'"
