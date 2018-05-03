# -*- coding: utf-8 -*-

import pymysql
import source_data.json_peon
import database.db_card_peon

JsonPeon = source_data.json_peon.JsonPeon()
DbCardPeon = database.db_card_peon.DbCardPeon()

if not JsonPeon.does_data_exist():
    print("No source_data found. Downloading card data.")
    JsonPeon.download_mtg_json()
else:
    print("Data already exists.")


data = JsonPeon.import_data()
sets = ['LEA']


DbCardPeon.reset_table('cards')

for set in sets:
    for card in data[set]["cards"]:
        DbCardPeon.add_card(card["name"])

DbCardPeon.close_connections()

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

