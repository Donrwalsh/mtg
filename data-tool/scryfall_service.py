import json
import os
import requests
from writer_service import Writer
from model.data_source import DataSource


class ScryfallService(DataSource):

    def __init__(self, **kwargs):
        self.local_storage = "data/scryfall/"
        self.api_url = "https://api.scryfall.com/"
        DataSource.__init__(self, 'Scryfall', **kwargs)

    def sets_initiate(self):
        if not self.set_data_exists() or self.update:
            Writer.option(Writer.pad_right("[download]", 13))
            self.download_set_data()
            return self.load_set_data()
        else:
            Writer.option(Writer.pad_right(" [local]", 13))
            return self.load_set_data()



    def load_set_data(self):
        with open(self.local_storage + 'sets.txt', 'r') as data_file:
            data = json.load(data_file)
        result = []
        for item in reversed(data):
            result.append(item)
        return result

    def download_set_data(self):
        r = requests.get(url=self.api_url + "sets")
        with open(self.local_storage + 'sets.txt', 'w') as outfile:
            json.dump(r.json()['data'], outfile)

    def set_data_exists(self):
        return os.path.isfile(self.local_storage + 'sets.txt')

    def set_data_date(self):
        return os.path.getmtime(self.local_storage + "sets.txt")
