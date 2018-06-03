import argparse
import scryfall_service
import database_service
import pprint
from writer_service import Writer

parser = argparse.ArgumentParser()
parser.add_argument("--update", help="force download of source data", action="store_true")
args = parser.parse_args()

Writer.action("DATA SOURCE |   SETS   | COUNT | \n")
Scryfall = scryfall_service.ScryfallService(update=args.update)
Database = database_service.DatabaseService(update=args.update)



primary = Scryfall.sets

# pprint.pprint(Database.sets)

# pprint.pprint(primary[0])
# pprint.pprint(primary[300])
# pprint.pprint(len(primary))

# for set in primary:
#     pprint.pprint(set)
#     exit()

# pprint.pprint(Scryfall.sets[0])


# Writer.action("Let's get started")
# pprint.pprint(time.struct_time(time_dif))

#
# for set in reversed(Scryfall.load_set_data()):
#     pprint.pprint(set)


# for set in reversed():
#     print(set)

    #TODO: Retrieve 3 different set data
    #TODO: Iterate over the primary source data:
        #TODO: Verify/add data to database
        #TODO: Report discrepencies

#Cards