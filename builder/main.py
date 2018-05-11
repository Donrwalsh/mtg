# -*- coding: utf-8 -*-
import random

import source.json_service
import database.database_service
from writer_service import Writer
import card_formatter
import argparse

sets = ['LEA', 'LEB', 'ARN', '2ED', 'pDRC', 'ATQ', '3ED', 'LEG', 'DRK', 'FEM', '4ED', 'ICE', 'CHR', 'HML', 'ALL', 'MIR',
        'VIS', '5ED', 'VAN', 'POR', 'WTH', 'TMP', 'STH', 'PO2', 'EXO', 'USG', 'ULG', '6ED', 'PTK', 'UDS', 'S99', 'MMQ',
        'BRB', 'NMS', 'PCY', 'BTD', 'INV', 'PLS', '7ED', 'APC', 'ODY', 'TOR', 'JUD', 'ONS', 'LGN', 'SCG', '8ED', 'MRD',
        'DST', '5DN', 'CHK', 'BOK', 'SOK', '9ED', 'RAV', 'GPT', 'DIS', 'CSP', 'TSB', 'TSP', 'PLC', 'FUT', '10E', 'MED',
        'LRW', 'EVG', 'MOR', 'SHM', 'EVE', 'DRB', 'ME2', 'ALA', 'DD2', 'CON', 'DDC', 'ARB', 'M10', 'V09', 'HOP', 'ME3',
        'ZEN', 'DDD', 'H09', 'WWK', 'DDE', 'ROE', 'ARC', 'M11', 'V10', 'DDF', 'SOM', 'PD2', 'ME4', 'MBS', 'DDG', 'NPH',
        'CMD', 'M12', 'V11', 'DDH', 'ISD', 'PD3', 'DKA', 'DDI', 'AVR', 'PC2', 'M13', 'V12', 'DDJ', 'RTR', 'CM1', 'GTC',
        'DDK', 'DGM', 'MMA', 'M14', 'V13', 'DDL', 'THS', 'C13', 'BNG', 'DDM', 'JOU', 'MD1', 'CNS', 'VMA', 'M15', 'V14',
        'DDN', 'KTK', 'C14', 'DD3_GVL', 'DD3_DVD', 'DD3_EVG', 'DD3_JVC', 'FRF_UGIN', 'FRF', 'DDO', 'DTK', 'TPR', 'MM2',
        'ORI', 'V15', 'DDP', 'EXP', 'BFZ', 'C15', 'OGW', 'DDQ', 'W16', 'SOI', 'EMA', 'EMN', 'V16', 'CN2', 'DDR', 'KLD',
        'MPS', 'C16', 'PCA', 'AER', 'MM3', 'DDS', 'AKH', 'MPS_AKH', 'C17', 'XLN', 'DDT', 'IMA', 'UST', 'RIX', 'A25',
        'DDU', 'DOM']

parser = argparse.ArgumentParser()
parser.add_argument("--build", help="destroy, then build the database", action="store_true")
parser.add_argument("--measure", help="find longest value in all current fields from json", action="store_true")
parser.add_argument("--random", help="display a random card in the console", action="store_true")
args = parser.parse_args()

JsonService = source.json_service.JsonService('source')
data = JsonService.import_data()
set_data = JsonService.create_set_data(data)
Database = database.database_service.DatabaseService()

# Conditional that decides whether or not to establish the database connection
if args.build:
    # Database.create_table('names')
    Database.build_database(sets, data, set_data)

if args.random:
    set_roll = random.randint(0, len(sets)-1)
    random_set = sets[set_roll]
    card_roll = random.randint(0, len(data[random_set]['cards'])-1)
    random_card = data[random_set]['cards'][card_roll]
    Writer.display_card(random_card, random_set)

if args.measure:
    JsonService.report_longest_values(sets)

# Database.close_connections()
