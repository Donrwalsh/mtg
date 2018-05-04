# -*- coding: utf-8 -*-
import source_data.json_peon
import database.db_card_peon

# Fore.LIGHTRED_EX for errors
# Fore.CYAN for informational notices only
# Fore.BLUE for actions being taken

sets = ['LEA']

# The JSON peon works with data from MTGJson
JsonPeon = source_data.json_peon.JsonPeon('source_data')
data = JsonPeon.import_data()

# The Database Peon works with our local database
DbCardPeon = database.db_card_peon.DbCardPeon()


