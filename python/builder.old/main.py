# -*- coding: utf-8 -*-
import argparse
import requests
import shutil
import os

import source.json_service
import database.database_service
from writer_service import Writer
from translator_service import TranslatorService
import source.image_service

# Command line invocations
parser = argparse.ArgumentParser()
parser.add_argument("--update", help="updates source data", action="store_true")
parser.add_argument("--build", help="destroy, then build the database", action="store_true")
parser.add_argument("--images", help="fetch images (in-progress", action="store_true")
parser.add_argument("--verbose", help="show too much information", action="store_true")
args = parser.parse_args()

JsonService = source.json_service.JsonService('source', update=args.update)
DatabaseService = database.database_service.DatabaseService(build=args.build, verbose=args.verbose)
ImageService = source.image_service.ImageService()

# Raw unmodified JSON data
DATA_CARDS = JsonService.import_data()
DATA_SETS = JsonService.create_set_data(DATA_CARDS)

# Drops and recreates the database tables if we are building.
if args.build:
    DatabaseService.build_database()

current_card_count = 0
previous_sets_total = 0

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
    img_count = 0
    for card in DATA_CARDS[set['code']]["cards"]:
        current_card_count += 1
        translated_card = TranslatorService(card)

        if args.build:
            DatabaseService.add_card(translated_card, str(s_index + 1))
            for field in ("names", "colors", 'colorIdentities', 'supertypes', 'types', 'subtypes'):
                DatabaseService.populate_normalized_table(translated_card, str(current_card_count), field)
            if card['name'] not in variant_builder:
                variant_builder[card['name']] = [current_card_count]
            else:
                for variant in variant_builder[card['name']]:
                    DatabaseService.add_variant(variant, current_card_count)
                variant_builder[card['name']].append(current_card_count)

        if args.images:
            if not ImageService.set_directory_exists(set['code']):
                ImageService.create_directory(set['code'])
            if not ImageService.image_exists(set['code'], current_card_count):
                try:
                    ImageService.fetch_image_by_multiverse_id(set['code'], card['multiverseid'], current_card_count)
                    img_count += 1
                except KeyError as e:
                    #TODO: Errors should be agregated and shown in the output somehow.
                    continue
            else:
                img_count += 1

    # Set output. Some fancy length-play going on for output depending on actions taken
    Writer.action_highlight_alternating(
        Writer.progress(s_index+1, len(DATA_SETS)) + " Synchronized " if args.build or args.images else " ",
        set['name'].replace('—', '-'),
        Writer.pad_right(".", 42 - len(set['name'])) + "| ",
        Writer.pad_right(str(current_card_count - previous_sets_total), 3),
        " | ",
        Writer.pad_right("DB_Added" if args.build else "DB_None", 10),
        "|  ",
        ("err" if img_count != (current_card_count - previous_sets_total) else "") + Writer.pad_right(str(img_count), 5),
        "| ",
        Writer.pad_right("IMG_Added" if args.images else "IMG_None", 11),
        "|"
    )
    previous_sets_total = current_card_count

DatabaseService.close_connections()