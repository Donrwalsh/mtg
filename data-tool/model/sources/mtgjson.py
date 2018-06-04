from urllib.request import urlretrieve
import urllib
import zipfile
import json
from model.data_source import DataSource
from writer_service import Writer
import os

class Mtgjson(DataSource):

    def __init__(self, **kwargs):
        self.local_storage = "data/mtgjson/"
        self.api_url = "https://mtgjson.com/json/AllSets-x.json.zip"
        DataSource.__init__(self, 'MTGJSON', **kwargs)

    def sets_initiate(self):
        if not self.set_data_exists() or self.update:
            Writer.option(Writer.pad_right("[download]", 13))
            self.download_set_data()
            return self.load_set_data()
        else:
            Writer.option(Writer.pad_right(" [local]", 13))
            return self.load_set_data()


    def load_set_data(self):
        with open(self.local_storage + 'sets.txt', encoding="utf8") as data_file:
            data = json.load(data_file)
        return data

    def download_set_data(self):
        try:
            urlretrieve(self.api_url, self.local_storage + "sets.zip")
        except urllib.error.HTTPError as e:
            Writer.error("Critical error retrieving source data", e)
            exit()
        zip_ref = zipfile.ZipFile(self.local_storage + "sets.zip", 'r')
        zip_ref.extractall(self.local_storage)
        zip_ref.close()
        os.rename(self.local_storage + "AllSets-x.json", self.local_storage + "sets.json")
        os.remove(self.local_storage + "sets.zip")
        # Remove cards from the set file:
        # TODO: The cards will need to be retained somehow.
        with open(self.local_storage + 'sets.json', encoding="utf8") as data_file:
            data = json.load(data_file)
        for set in data:
            data[set].pop('cards')
        with open(self.local_storage + 'sets.txt', 'w') as outfile:
            json.dump(data, outfile)
        os.remove(self.local_storage + "sets.json")

    def set_data_exists(self):
        return os.path.isfile(self.local_storage + 'sets.txt')

    def set_by_code(self, code):
        return self.sets[code.upper()]
