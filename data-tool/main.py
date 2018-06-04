import argparse
from model.sources import scryfall, database
import pprint
from writer_service import Writer

parser = argparse.ArgumentParser()
parser.add_argument("--update", help="force download of source data", action="store_true")
args = parser.parse_args()

Writer.action("DATA SOURCE |   SETS   | COUNT | \n")
Scryfall = scryfall.Scryfall(update=args.update)
Database = database.Database(update=args.update)



primary = Scryfall.sets

for set in primary:

    #Look for set in database
    try:
        Database.set_by_code(set['code'])
        #TODO: The set exists, verify the set's contents.
    except StopIteration:
        #TODO: The set does not exist. Add the set.
        print("Set does not exist")
    exit()
