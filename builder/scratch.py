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


# def f(*args, **kwargs):
#    print('args: ', args, ' kwargs: ', kwargs)
#
# f('a')
# f(ar='a')
# f(1,2,param=3)
# #
# #
# #
# #
# exit()
#
JsonService = source.json_service.JsonService('source')
data = JsonService.import_data()
DATA_SETS = JsonService.create_set_data(data)
max = 0
for set in DATA_SETS:
   if len(set['name']) > max:
      print(set['name'])
      max = len(set['name'])
print(max)
# DbCardPeon = database.database_service.DatabaseService()
#
# data = JsonPeon.import_data()
#
# # JsonPeon.report_longest_values(sets)
# # exit()
# #
# # rarities = []
# # j = 0
# # for set in data:
# #     for card in data[set]['cards']:
# #         if 'timeshifted' in card:
# #             print(card['timeshifted'])
# #
# # print(j)
# # exit()
#
# pprint.pprint(rarities)
#
# # pprint.pprint(JsonPeon.create_set_data(data))
# # d_output = {}
# # output = []
# #
# # for set in data:
# #
# #     d_addition = {'set': set, 'date': data[set]['releaseDate']}
# #     # addition = (set, data[set]['releaseDate'])
# #     output.append(d_addition)
# #
# #
# #
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

