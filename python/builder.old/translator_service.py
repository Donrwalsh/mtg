
class TranslatorService(object):

    colorMap = {
        "W": "White",
        "U": "Blue",
        "B": "Black",
        "R": "Red",
        "G": "Green",
    }

    def __init__(self, card):
        self.card = card
        self.db = {
            'name': self.single_value_str('name'),
            'names': self.multi_value_str('names'),
            'manaCost': self.single_value_str('manaCost'),
            'cmc': self.single_value_int('cmc'),
            'colors': self.multi_value_str('colors'),
            'colorIdentities': self.multi_value_str('colorIdentity'),
            'supertypes': self.multi_value_str('supertypes'),
            'types': self.multi_value_str('types'),
            'subtypes': self.multi_value_str('subtypes'),
            'rarity': self.single_value_str('rarity'),
            'text': self.single_value_str('text'),
            'flavor': self.single_value_str('flavor'),
            'artist': self.single_value_str('artist'),
            'number': self.single_value_str('number'),
            'power': self.single_value_str('power'),
            'toughness': self.single_value_str('toughness'),
            'loyalty': self.single_value_str('loyalty'),
            'multiverseid': self.single_value_int('multiverseid'),
            'variations': self.multi_value_int('variations'),
            'watermark': self.single_value_str('watermark'),
            'border': self.single_value_str('border'),
            'layout': self.single_value_str('layout'),
            'timeshifted': self.single_value_bool('timeshifted'),
            'reserved': self.single_value_bool('reserved'),
            'starter': self.single_value_bool('starter')
        }

    def single_value_str(self, field):
        if field in self.card:
            return "'" + str(self.card[field]).replace("'", "''") + "'"
        else:
            return "null"

    def single_value_int(self, field):
        if field in self.card:
            return str(self.card[field])
        else:
            return "null"

    def single_value_bool(self, field):
        if field in self.card:
            return '1'
        else:
            return '0'

    def multi_value_str(self, field):
        result = []
        if field in self.card:
            for item in self.card[field]:
                if field == 'colorIdentity':
                    item = self.colorMap[item]
                result.append("'" + str(item).replace("'", "''") + "'")
            return result
        else:
            return False if field not in ['colors', 'colorIdentity'] else ["'Colorless'"]

    def multi_value_int(self, field):
        result = []
        if field in self.card:
            for item in self.card[field]:
                result.append(str(item))
        return result

