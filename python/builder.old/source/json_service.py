from urllib.request import urlretrieve
import urllib
import zipfile
import json
import os

from writer_service import Writer


class JsonService:

    def __init__(self, dir, **kwargs):
        self.location = dir + '/AllSets-x.json'

        if kwargs.get('update'):
            self.download_mtg_json(dir, 'Update requested.')
        else:
            if not os.path.isfile(self.location):
                self.download_mtg_json(dir, "No source found.")
            else:
                Writer.note("Source_data already exists.")

    def download_mtg_json(self, dir, msg):
        Writer.action(msg + " Downloading latest card data.")
        try:
            urlretrieve("http://www.mtgjson.com/json/AllSets-x.json.zip", self.location + ".zip")
        except urllib.error.HTTPError as e:
            Writer.error("Critical error retrieving source data", e)
            exit()
        zip_ref = zipfile.ZipFile(self.location + ".zip", 'r')
        zip_ref.extractall(dir)
        zip_ref.close()
        os.remove(self.location + ".zip")
        Writer.action_with_highlight("Source data downloaded to ", self.location, ".")

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
