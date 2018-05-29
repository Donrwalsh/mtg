# -*- coding: utf-8 -*-
import argparse
import requests
import shutil
import pprint
import os

import source.json_service
import database.database_service
from writer_service import Writer
from translator_service import TranslatorService

# Command line invocations
parser = argparse.ArgumentParser()
parser.add_argument("--update", help="updates source data", action="store_true")
parser.add_argument("--build", help="destroy, then build the database", action="store_true")
parser.add_argument("--images", help="fetch images (in-progress", action="store_true")
parser.add_argument("--verbose", help="show too much information", action="store_true")
args = parser.parse_args()

JsonService = source.json_service.JsonService('source', update=args.update)
DatabaseService = database.database_service.DatabaseService(build=args.build, verbose=args.verbose)

# Raw unmodified JSON data
DATA_CARDS = JsonService.import_data()
DATA_SETS = JsonService.create_set_data(DATA_CARDS)

# Drops and recreates the database tables if we are building.
if args.build:
    DatabaseService.build_database(DATA_CARDS, DATA_SETS)

i, j = 0, 0                 # 'i' tracks current card, 'j' checkpoints last completed set
variant_builder = {}        # only used when building

# Output header
if args.build or args.images:
    Writer.action_with_highlight_stub("[", " PROGRESS ", "]" + " " * 56)
else:
    Writer.action_stub(" " * 43)

Writer.action_highlight_alternating("|", "CARDS", "|", " DB_ACTION ", "|", " IMAGES", "|", " IMG_ACTION ", "|",)

# Main street
for s_index, set in enumerate(DATA_SETS):
    if args.build:
        DatabaseService.add_set(set)
    for card in DATA_CARDS[set['code']]["cards"]:
        i += 1
        translated_card = TranslatorService(card)

        DatabaseService.add_card(translated_card, str(s_index + 1))
        for field in ("names", "colors", 'colorIdentities', 'supertypes', 'types', 'subtypes'):
            DatabaseService.populate_normalized_table(translated_card, str(i), field)
        if args.build:
            if card['name'] not in variant_builder:
                variant_builder[card['name']] = [i]
            else:
                for variant in variant_builder[card['name']]:
                    DatabaseService.query(
                        "INSERT INTO variations (card_id, variant_id) VALUES (" + str(variant) + ", " + str(i) + ");")
                    DatabaseService.query(
                        "INSERT INTO variations (card_id, variant_id) VALUES (" + str(i) + ", " + str(variant) + ");")
                variant_builder[card['name']].append(i)

    # Set output. Some fancy length-play going on for output depending on actions taken
    Writer.action_highlight_alternating(
        Writer.progress(s_index+1, len(DATA_SETS)) + " Synchronized " if args.build else " ",
        set['name'].replace('—', '-'),
        Writer.pad_right(".", 42 - len(set['name'])) + "| ",
        Writer.pad_right(str(i - j), 3),
        " | ",
        Writer.pad_right("DB_Added" if args.build else "DB_None", 10),
        "|  ",
        Writer.pad_right("num", 5),
        "| ",
        Writer.pad_right("IMG_Added" if args.images else "IMG_None", 11),
        "|"
    )
    j = i

# Images is not part of the main loop, but should be.
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