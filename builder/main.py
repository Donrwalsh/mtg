# -*- coding: utf-8 -*-
import source.json_service
import database.database_service
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
args = parser.parse_args()

if args.build:
    DatabaseService.build_database(DATA_CARDS, DATA_SETS)
