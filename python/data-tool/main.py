import argparse
from urllib.request import urlretrieve
import os
from model.sources import scryfall, mtgjson, database
import pprint
from writer_service import Writer
from helper_service import Helper

parser = argparse.ArgumentParser()
parser.add_argument("--update", help="force download of source data", action="store_true")
args = parser.parse_args()

Writer.action("DATA SOURCE |   SETS   | COUNT | \n")
Scryfall = scryfall.Scryfall(update=args.update)
Mtgjson = mtgjson.Mtgjson(update=args.update)
Database = database.Database()



primary = Scryfall.sets

for set in primary:
    try:
        set_2 = Mtgjson.set_by_code(set['code'])
    except KeyError:
        set_2 = {}

    #Look for set in database
    try:
        if not Helper.validate_set(Database.set_by_code(set['code']), [set, set_2]):
            print("I found a problem")
        #TODO: The set exists, verify the set's contents.
    except StopIteration:
        Database.add_set([set, set_2])

    # Set Images
    svg_img_dir = '../src/main/resources/static/images/sets/'
    if not os.path.isdir(svg_img_dir):
        os.makedirs("../src/main/resources/static/images/sets/")

    svg_img_path = svg_img_dir + (set['code'] if set['code'] != 'con' else '_' + set['code']) + '.svg'
    if not os.path.isfile(svg_img_path):
        urlretrieve(set['icon_svg_uri'], svg_img_path)


    # else:
    #     pprint.pprint("set icon exists")

    # pprint.pprint(os.getcwd())
    # pprint.pprint(os.path.isfile(''))
    # pprint.pprint(set)
    # exit()
