from urllib.request import urlretrieve
import urllib
import zipfile
import json
import os

from writer_service import Writer
import card_formatter


class JsonService:

    def __init__(self, dir):
        self.location = dir + '/AllSets-x.json'
        if not os.path.isfile(self.location):
            Writer.action("No source found. Downloading card data.")
            try:
                urlretrieve("http://www.mtgjson.com/json/AllSets-x.json.zip", self.location + ".zip")
            except urllib.error.HTTPError as e:
                Writer.error("Critical error retrieving source data", e)
                exit()
            zip_ref = zipfile.ZipFile(self.location + ".zip", 'r')
            zip_ref.extractall(dir)
            zip_ref.close()
            os.remove(self.location + ".zip")
            Writer.action("Source data downloaded to " + self.location)
        else:
            Writer.note("Source_data already exists.")

    def import_data(self):
        with open(self.location, encoding="utf8") as data_file:
            data = json.load(data_file)
        return data

    # Leaves out block and booster
    def create_set_data(self, data):
        output = []
        for set in data:
            output.append({
                'name': data[set]['name'],
                'code': data[set]['code'],
                'releaseDate': data[set]['releaseDate'],
                'border': data[set]['border'],
                'type': data[set]['type'],
                'onlineOnly': data[set]['onlineOnly'] if 'onlineOnly' in data[set] else "false"
            })
        output.sort(key=lambda x: x['releaseDate'])
        return output


    def longest_value(self, sets, field):
        db_max_length = 0
        db_max_value = ""
        console_max_length = 0
        console_max_value = ""
        data = self.import_data()
        for set in sets:
            for card in data[set]['cards']:
                Formatter = card_formatter.CardFormatter(card)
                db_value = Formatter.db[field]
                console_value = Formatter.console[field]
                if len(str(db_value)) > db_max_length:
                    db_max_value = db_value
                    db_max_length = len(str(db_value))
                if len(str(console_value)) > console_max_length:
                    console_max_value = console_value
                    console_max_length = len(str(console_value))
        return {'c_value': str(console_max_value),
                'c_length': console_max_length,
                'd_value': str(db_max_value),
                'd_length': db_max_length}

    def report_longest_values(self, sets):
        field_length = 14
        type_length = 8
        max_length = 5
        fields = ['name', 'names', 'colors', 'colorIdentity', 'manaCost', 'cmc', 'type', 'supertypes', 'types',
                  'subtypes', 'rarity']

        Writer.note("=============== Measure Report ===============")

        Writer.note_stub("|")
        Writer.highlight_stub(Writer.pad_both("FIELD", field_length + 1))
        Writer.note_stub("|")
        Writer.highlight_stub(Writer.pad_both("TYPE", type_length + 1))
        Writer.note_stub("|")
        Writer.highlight_stub(Writer.pad_both("MAX", max_length))
        Writer.note_with_highlight("| ", "VALUE", "")
        for field in fields:
            values = self.longest_value(sets, field)
            Writer.note_stub("|")
            Writer.highlight_stub(Writer.pad_left(field, field_length))
            Writer.note_stub(" |")
            Writer.highlight_stub(Writer.pad_left("db", type_length))
            Writer.note_stub(" |")
            Writer.highlight_stub(Writer.pad_both(str(values['d_length']), max_length))
            Writer.note_with_highlight("| ", values['d_value'], "")

            Writer.note_stub("|")
            Writer.highlight_stub(Writer.pad_left("", field_length))
            Writer.note_stub(" |")
            Writer.highlight_stub(Writer.pad_both("console", type_length))
            Writer.note_stub(" |")
            Writer.highlight_stub(Writer.pad_both(str(values['c_length']), max_length))
            Writer.note_with_highlight("| ", values['c_value'], "")

            # print(values)
        # fields = ['name', 'names', 'manaCost', 'cmc']
        # for field in fields[::-1]:
        #     print(self.longest_value(sets, field))
