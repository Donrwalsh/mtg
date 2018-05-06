# -*- coding: utf-8 -*-

import pymysql
import source_data.json_peon
import database.db_card_peon
from pprint import pprint

JsonPeon = source_data.json_peon.JsonPeon('source_data')
DbCardPeon = database.db_card_peon.DbCardPeon()

data = JsonPeon.import_data()
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

max_length = 0


for item in data["LEA"]:
    if item is not "cards":
        pprint(data["LEA"][item])


# JsonPeon.report_longest_values(sets)

#
#
# DbCardPeon.reset_table('cards')
#
# for set in sets:
#     for card in data[set]["cards"]:
#         DbCardPeon.add_card(card["name"])
#
# DbCardPeon.close_connections()

# conn.commit()
# cur.close()
# conn.close()

# cur.execute("SELECT * FROM user")
# for response in cur:
#     print(response)
# cur.close()
# conn.close()


# for set in sets:
#     for card in data[set]["cards"]:
#         print(card["name"])




#
#
# for set in source_data:
#     print(set)

# for set in sets:
#     for card in source_data[set]["cards"]:
#         print(card['name'])

