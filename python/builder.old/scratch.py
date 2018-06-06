import requests
import pprint
from mtgsdk import Set
import json

def call_to_json(url):
    r = requests.get(url=url)
    return r.json()['data']

with open('data.txt', 'w') as outfile:
    json.dump(call_to_json('https://api.scryfall.com/sets'), outfile)

with open('data.txt', encoding="utf8") as data_file:
    data = json.load(data_file)

pprint.pprint(data)

# set = Set.find('ktk')
# pprint.pprint(set.booster)



#
# sets = call_to_json('https://api.scryfall.com/sets')
# pprint.pprint(sets)
# for i in reversed(sets):
#     pprint.pprint(i['code'])



#
# https://api.scryfall.com/cards/xln/96
