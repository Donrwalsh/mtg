import os
import requests
import shutil


class ImageService(object):

    def __init__(self, **kwargs):
        self.verbose = True if kwargs.get('verbose') else False

        self.location = '../images/'

    def set_directory_exists(self, set_code):
        return os.path.exists(self.location + set_code + '/')

    def image_exists(self, set_code, id):
        return os.path.exists(self.location + set_code + '/' + str(id) + '.jpg')

    def create_directory(self, set_code):
        os.makedirs(self.location + set_code + '/')

    def fetch_image_by_multiverse_id(self, set_code, multiverseid, id):
        r = requests.get(url='https://api.scryfall.com/cards/multiverse/' + str(multiverseid))
        url = r.json()['image_uris']['normal']
        response = requests.get(url, stream=True)
        with open('../images/' + set_code + '/' + str(id) + '.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
