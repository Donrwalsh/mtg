# -*- coding: utf-8 -*-

import random
import sys
from colorama import Fore
from colorama import Style
import source.json_service
import database.database_service
from pprint import pprint
from writer_service import Writer
import pprint

JsonPeon = source.json_service.JsonService('source')
DbCardPeon = database.database_service.DatabaseService()

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

# JsonPeon.report_longest_values(sets)
# exit()

rarities = []
j = 0
for set in data:
    for card in data[set]['cards']:
        if 'timeshifted' in card:
            print(card['timeshifted'])

print(j)
exit()

pprint.pprint(rarities)

# pprint.pprint(JsonPeon.create_set_data(data))
# d_output = {}
# output = []
#
# for set in data:
#
#     d_addition = {'set': set, 'date': data[set]['releaseDate']}
#     # addition = (set, data[set]['releaseDate'])
#     output.append(d_addition)
#
#
#
# pprint.pprint(output)




#
# j = 0
# while True:
#     j += 1
#     set_roll = random.randint(0, len(sets)-1)
#     random_set = sets[set_roll]
#     card_roll = random.randint(0, len(data[random_set]['cards'])-1)
#     random_card = data[random_set]['cards'][card_roll]
#     if "colorIdentity" not in random_card:
#         Writer.display_card(random_card, random_set)
#         exit()
    # if "manaCost" in random_card:
    #     print(f"{Fore.WHITE}manaCost {Fore.YELLOW}" + random_card["manaCost"])
    #     random_card.pop('manaCost')
    # else:
    #     print(f"{Fore.WHITE}manaCost {Fore.YELLOW}null")
    # if "cmc" in random_card:
    #     print(f"{Fore.WHITE}cmc      {Fore.YELLOW}" + str(random_card["cmc"]))
    #     random_card.pop("cmc")
    # else:
    #     print(f"{Fore.WHITE}cmc      {Fore.YELLOW}null")
    # print(f"{Fore.WHITE}set      {Fore.YELLOW}" + random_set)
    # if "colors" in random_card:
    #     i = 0
    #     sys.stdout.write(f"{Fore.WHITE}colors   ")
    #     for item in random_card['colors']:
    #         i += 1
    #         sys.stdout.write(f"{Fore.YELLOW}" + item)
    #         if i < len(random_card['colors']):
    #             sys.stdout.write(', ')
    #         else:
    #             sys.stdout.write('\n')
    #     random_card.pop('colors', None)
    # else:
    #     print(f"{Fore.WHITE}colors   {Fore.YELLOW}null")
    # print(random_card)
    # print(f"{Fore.LIGHTWHITE_EX}----------------------------------------------------------------------------------")


# for x in range(10):
#   print(random.randint(1,101))






#
# for item in data["LEA"]:
#     if item is not "cards":
#         pprint(data["LEA"][item])


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
# for set in source:
#     print(set)

# for set in sets:
#     for card in source[set]["cards"]:
#         print(card['name'])

