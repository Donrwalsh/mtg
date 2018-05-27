# -*- coding: utf-8 -*-
import source.json_service
import database.database_service
import argparse
import requests
import shutil
import pprint
import os

# Command-Line invocations
from writer_service import Writer

parser = argparse.ArgumentParser()

parser.add_argument("--verify", help="Verifies nothing, but will", action="store_true")
parser.add_argument("--build", help="destroy, then build the database", action="store_true")
parser.add_argument("--images", help="fetch images (in-progress", action="store_true")

args = parser.parse_args()

# if args.verify:
# Verify the MTGJSON data is the latest release.
# Verify the Databsae (in tiers):
# Verify the number of cards matches mtgJSON data.


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
    DatabaseService.query("SELECT cards.id, cards.multiverseid, `sets`.code, cards.layout FROM `sets` INNER JOIN cards ON "
                          "sets.id=cards.`set`")
    id_map = DatabaseService.cur.fetchall()
    for trip in id_map:
        # Skipped certain cards due to complications to sort out later.
        if not trip[2] in ('VAN') and trip[3] != "token" and trip[3] != 'split' and trip[3] != 'double-faced':
            if trip[1] is not None:
                pprint.pprint("Current Trip: " + str(trip))
                if not os.path.exists('../images/' + trip[2] + '/'):
                    os.makedirs('../images/' + trip[2] + '/')
                if not os.path.exists('../images/' + trip[2] + '/' + str(trip[0]) + '.jpg'):
                    try:
                        r = requests.get(url='https://api.scryfall.com/cards/multiverse/' + str(trip[1]))
                        url = r.json()['image_uris']['normal']
                        response = requests.get(url, stream=True)
                        with open('../images/' + trip[2] + '/' + str(trip[0]) + '.jpg', 'wb') as out_file:
                            shutil.copyfileobj(response.raw, out_file)
                    except KeyError as e:
                        Writer.error("An error occurred when retrieving image:", e)
                        # The following trip causes an error. Not sure why yet.
                        # 'image_uris'"Current Trip: (35679, 442789, 'DDU', 'normal')"