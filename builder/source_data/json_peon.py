import collections
from urllib.request import urlretrieve
import zipfile
import json
import os
from colorama import Fore
from colorama import Style


class JsonPeon:

    def __init__(self, dir):
        self.location = dir + '/AllSets-x.json'
        if not os.path.isfile(self.location):
            print(f"{Fore.BLUE}No source_data found. Downloading card data.")
            urlretrieve("http://www.mtgjson.com/json/AllSets-x.json.zip", self.location + ".zip")
            zip_ref = zipfile.ZipFile(self.location + ".zip", 'r')
            zip_ref.extractall(dir)
            zip_ref.close()
            os.remove(self.location + ".zip")
            print(f"Source data downloaded to " + self.location + "f{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Source_data already exists.{Style.RESET_ALL}")

    def import_data(self):
        with open(self.location, encoding="utf8") as data_file:
            data = json.load(data_file)
        return data

    def longest_value(self, sets, field):
        max_length = 0
        max_value = ""
        data = self.import_data()
        for set in sets:
            for card in data[set]['cards']:
                if field in card:
                    if field == "names":
                        value = self.multi_value_translate(card[field])
                        if len(value) > max_length:
                            max_length = len(value)
                            max_value = value
                    else:
                        if len(str(card[field])) > max_length:
                            max_length = len(str(card[field]))
                            max_value = card[field]
        return field, max_length, max_value

    def report_longest_values(self, sets):
        fields = ['name', 'names', 'manaCost', 'cmc']
        for field in fields[::-1]:
            print(self.longest_value(sets, field))

    def multi_value_translate(self, array):
        result = "'"
        i = 0
        for item in array:
            i += 1
            result += item.replace("'", "''")
            if i < len(array):
                result += "//"
        result += "'"
        return result