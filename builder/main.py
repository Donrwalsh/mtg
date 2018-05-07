# -*- coding: utf-8 -*-
import source.json_service
import database.database_service

from colorama import Fore
from colorama import Style

# Fore.LIGHTRED_EX for errors
# Fore.CYAN for informational notices only
# Fore.BLUE for actions being taken
# Fore.YELLOW for calling out individual items
import card_formatter


def progress(current, total):
    bars = int((current/total)*10)
    return "[" + bars * "-" + (10-bars)*" " + "]"


sets = ['LEA', 'LEB', 'ARN', '2ED', 'pDRC', 'ATQ', '3ED', 'LEG', 'DRK', 'FEM', '4ED',
        'ICE', 'CHR', 'HML', 'ALL', 'MIR', 'VIS', '5ED', 'VAN', 'POR',
        'WTH', 'TMP', 'STH', 'PO2', 'EXO', 'USG', 'ULG', '6ED', 'PTK', 'UDS',
        'S99', 'MMQ', 'BRB', 'NMS', 'PCY', 'BTD', 'INV', 'PLS',
        '7ED', 'APC', 'ODY', 'TOR', 'JUD', 'ONS', 'LGN', 'SCG', '8ED', 'MRD', 'DST', '5DN',
        'CHK', 'BOK', 'SOK', '9ED', 'RAV', 'GPT', 'DIS', 'CSP', 'TSB', 'TSP',
        'PLC', 'FUT', '10E', 'MED', 'LRW', 'EVG', 'MOR', 'SHM',
        'EVE', 'DRB', 'ME2', 'ALA', 'DD2', 'CON', 'DDC', 'ARB', 'M10', 'V09', 'HOP', 'ME3', 'ZEN', 'DDD', 'H09',
        'WWK', 'DDE', 'ROE', 'ARC', 'M11', 'V10', 'DDF', 'SOM', 'PD2', 'ME4', 'MBS', 'DDG', 'NPH', 'CMD', 'M12',
        'V11', 'DDH', 'ISD', 'PD3', 'DKA', 'DDI', 'AVR', 'PC2', 'M13', 'V12', 'DDJ', 'RTR', 'CM1', 'GTC', 'DDK',
        'DGM', 'MMA', 'M14', 'V13', 'DDL', 'THS', 'C13', 'BNG', 'DDM', 'JOU', 'MD1', 'CNS', 'VMA', 'M15', 'V14',
        'DDN', 'KTK', 'C14', 'DD3_GVL', 'DD3_DVD', 'DD3_EVG', 'DD3_JVC', 'FRF_UGIN', 'FRF', 'DDO', 'DTK', 'TPR', 'MM2',
        'ORI', 'V15', 'DDP', 'EXP', 'BFZ', 'C15', 'OGW', 'DDQ', 'W16', 'SOI', 'EMA', 'EMN', 'V16', 'CN2', 'DDR', 'KLD',
        'MPS', 'C16', 'PCA', 'AER', 'MM3', 'DDS', 'AKH', 'MPS_AKH', 'C17', 'XLN', 'DDT', 'IMA', 'UST', 'RIX', 'A25',
        'DDU', 'DOM'  ]


# The JSON peon works with data from MTGJson
JsonService = source.json_service.JsonService('source')
data = JsonService.import_data()

# The Database Peon works with our local database
Database = database.database_service.DatabaseService()
Database.wipe_table('cards')


i = 0
for set in sets:
    i += 1
    print(f"{Fore.BLUE}" + progress(i, len(sets)) + f"Synchronizing {Fore.YELLOW}" + set + f"{Fore.BLUE}.")
    for card in data[set]["cards"]:
        TranslatePeon = card_formatter.CardFormatter(card)
        Database.add_card(
            TranslatePeon.name_for_db(),
            TranslatePeon.names_for_db(),
            TranslatePeon.mana_cost_for_db(),
            TranslatePeon.cmc_for_db(),
            "'" + set + "'",
            TranslatePeon.colors_for_db(),
            TranslatePeon.color_identity_for_db()
        )

Database.close_connections()