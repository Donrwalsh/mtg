import argparse
from model.sources import scryfall, database
import pprint
from writer_service import Writer
from helper_service import Helper

parser = argparse.ArgumentParser()
parser.add_argument("--update", help="force download of source data", action="store_true")
args = parser.parse_args()

Writer.action("DATA SOURCE |   SETS   | COUNT | \n")
Scryfall = scryfall.Scryfall(update=args.update)
Database = database.Database()



primary = Scryfall.sets

for set in primary:

    # pprint.pprint(set)

    # pprint.pprint(Database.set_by_code(set['code']))
    # exit()

    #Look for set in database
    try:
        if not Helper.validate_set(Database.set_by_code(set['code']), [set]):
            print("I found a problem")
        #TODO: The set exists, verify the set's contents.
    except StopIteration:
        Database.add_set([set])
