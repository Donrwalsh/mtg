from urllib.request import urlretrieve
import zipfile
import json
import os


class JsonPeon:

    @staticmethod
    def does_data_exist():
        return os.path.isfile('source_data/AllSets-x.json')

    @staticmethod
    def download_mtg_json():
        urlretrieve("http://www.mtgjson.com/json/AllSets-x.json.zip", "source_data/AllSets-x.json.zip")
        zip_ref = zipfile.ZipFile("source_data/AllSets-x.json.zip", 'r')
        zip_ref.extractall('source_data/')
        zip_ref.close()
        os.remove("source_data/AllSets-x.json.zip")

    @staticmethod
    def import_data():
        with open('source_data/AllSets-x.json', encoding="utf8") as data_file:
            data = json.load(data_file)
        return data
