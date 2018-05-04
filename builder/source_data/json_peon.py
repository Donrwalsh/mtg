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
        with open('source_data/AllSets-x.json', encoding="utf8") as data_file:
            data = json.load(data_file)
        return data
