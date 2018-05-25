# -*- coding: utf-8 -*-
import source.json_service
import database.database_service
import argparse
import requests
import shutil
import pprint
import os

# Command-Line invocations
parser = argparse.ArgumentParser()
parser.add_argument("--build", help="destroy, then build the database", action="store_true")
parser.add_argument("--images", help="fetch images (in-progress", action="store_true")
args = parser.parse_args()

JsonService = source.json_service.JsonService('source')
DatabaseService = database.database_service.DatabaseService()

# Raw unmodified JSON data
DATA_CARDS = JsonService.import_data()
DATA_SETS = JsonService.create_set_data(DATA_CARDS)

# List of set codes. Used frequently for iteration
SETS = []
for set in DATA_SETS:
    SETS.append(set['code'])

if args.build:
    DatabaseService.build_database(DATA_CARDS, DATA_SETS)

if args.images:
    DatabaseService.query("SELECT cards.id, cards.multiverseid, `sets`.code FROM `sets` INNER JOIN cards ON "
                          "sets.id=cards.`set`")
    id_map = DatabaseService.cur.fetchall()
    for trip in id_map:
        if trip[1] is not 'null':
            r = requests.get(url='https://api.scryfall.com/cards/multiverse/' + str(trip[1]))
            print("Downloading " + r.name + " from " + r.set_name)
            pprint.pprint(r)
            exit()
            url = r.json()['image_uris']['png']
            response = requests.get(url, stream=True)
            if not os.path.exists('../' + trip[2] + '/'):
                os.makedirs('../' + trip[2] + '/')
            with open('../images/' + trip[2] + '/' + str(trip[0]) + '.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)