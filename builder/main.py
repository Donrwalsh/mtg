# -*- coding: utf-8 -*-
import random
import source.json_service
import database.database_service
from writer_service import Writer
import argparse
JsonService = source.json_service.JsonService('source')
DatabaseService = database.database_service.DatabaseService()

# Raw unmodified JSON data
DATA_CARDS = JsonService.import_data()
DATA_SETS = JsonService.create_set_data(DATA_CARDS)

# List of set codes. Used frequently for iteration
SETS = []
for set in DATA_SETS:
    SETS.append(set['code'])

parser = argparse.ArgumentParser()
parser.add_argument("--build", help="destroy, then build the database", action="store_true")
parser.add_argument("--measure", help="find longest value in all current fields from json", action="store_true")
parser.add_argument("--random", help="display a random card in the console", action="store_true")
args = parser.parse_args()

if args.build:
    DatabaseService.build_database(DATA_CARDS, DATA_SETS)

if args.random:
    set_roll = random.randint(0, len(SETS)-1)
    random_set = SETS[set_roll]
    card_roll = random.randint(0, len(DATA_CARDS[random_set]['cards']) - 1)
    random_card = DATA_CARDS[random_set]['cards'][card_roll]
    Writer.display_card(random_card, random_set)

if args.measure:
    JsonService.report_longest_values(SETS)

# Database.close_connections()
