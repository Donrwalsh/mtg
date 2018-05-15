import pymysql
import database.identity
from writer_service import Writer
import translator_service


class DatabaseService(object):
    tables = ('cards', 'names', 'sets', 'colors', 'color_identities', 'supertypes', 'types', 'subtypes', 'variations')

    def __init__(self):
        try:
            self.conn = pymysql.connect(host=database.identity.host,
                                        user=database.identity.user,
                                        passwd=database.identity.passwd,
                                        db=database.identity.db)
            self.cur = self.conn.cursor()
        except pymysql.err.DatabaseError as e:
            Writer.error("Critical error connecting to database", e)
            exit()
        else:
            Writer.action("Connected to database.")
        self.conn.set_charset('utf8')

    def query(self, query):
        try:
            self.cur.execute(query)
        except pymysql.err.DatabaseError as e:
            Writer.SQL_error("Critical error working with database:", e, query)
            exit()
        except UnicodeEncodeError as e:
            Writer.SQL_error("Critical encoding error:", e, query)
            exit()

    def create_table(self, table_name):
        if table_name == 'cards':
            self.query("""CREATE TABLE `cards` (
                                      `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT, 
                                      `name` varchar(150) NOT NULL,
                                      `manaCost` varchar(45) DEFAULT NULL,
                                      `cmc` int(11) DEFAULT NULL,
                                      `set` int(11) NOT NULL,
                                      `rarity` varchar(15) NOT NULL,
                                      `text` VARCHAR(800),
                                      `flavor` VARCHAR(500),
                                      `artist` VARCHAR(100),
                                      `number` VARCHAR(10),
                                      `power` VARCHAR(10),
                                      `toughness` VARCHAR(10),
                                      `loyalty` VARCHAR(10),
                                      `multiverseid` int(11) unsigned,
                                      `watermark` VARCHAR(50),
                                      `border` VARCHAR(20),
                                      `layout` VARCHAR(20),
                                      `timeshifted` TINYINT(1),
                                      `reserved` TINYINT(1),
                                      `starter` TINYINT(1),
                                      PRIMARY KEY (`id`)
                                      ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;""")
        elif table_name == "names":
            self.query("""CREATE TABLE `names` (
                                      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                      `card` int(11) unsigned NOT NULL,
                                      `name` VARCHAR(50) NOT NULL,
                                      PRIMARY KEY (`id`)
                                      ) ENGINE=InnoDB DEFAULT CHARSET=utf8; """)
        elif table_name == "sets":
            self.query("""CREATE TABLE `sets` (
                                      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                      `name` VARCHAR(50) NOT NULL,
                                      `code` VARCHAR(10) NOT NULL,
                                      `releaseDate` DATE NOT NULL,
                                      `border` VARCHAR(50) NOT NULL,
                                      `type` VARCHAR(50) NOT NULL,
                                      `onlineOnly` TINYINT(1) NOT NULL,
                                      PRIMARY KEY (`id`)
                                      ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
        elif table_name == "colors":
            self.query("""CREATE TABLE `colors` (
                                      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                      `card_id` int(11) unsigned NOT NULL,
                                      `color` VARCHAR(10) NOT NULL,
                                      PRIMARY KEY (`id`)
                                      ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
        elif table_name == "color_identities":
            self.query("""CREATE TABLE `color_identities` (
                                      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                      `card_id` int(11) unsigned NOT NULL,
                                      `color` VARCHAR(10) NOT NULL,
                                      PRIMARY KEY (`id`)
                                      ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
        elif table_name == "supertypes":
            self.query("""CREATE TABLE `supertypes` (
                                      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                      `card_id` int(11) unsigned NOT NULL,
                                      `supertype` VARCHAR(10) NOT NULL,
                                      PRIMARY KEY (`id`)
                                      ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
        elif table_name == "types":
            self.query("""CREATE TABLE `types` (
                                      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                      `card_id` int(11) unsigned NOT NULL,
                                      `type` VARCHAR(20) NOT NULL,
                                      PRIMARY KEY (`id`)
                                      ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
        elif table_name == "subtypes":
            self.query("""CREATE TABLE `subtypes` (
                                      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                      `card_id` int(11) unsigned NOT NULL,
                                      `subtype` VARCHAR(25) NOT NULL,
                                      PRIMARY KEY (`id`)
                                      ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
        elif table_name == "variations":
            self.query("""CREATE TABLE `variations` (
                                      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                      `card_id` int(11) unsigned NOT NULL,
                                      `variant_id` int(11) unsigned NOT NULL,
                                      PRIMARY KEY (`id`)
                                      ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
        Writer.action_with_highlight("Table `", table_name, "` has been created.")

    def drop_table(self, table_name):
        try:
            self.cur.execute("DROP TABLE IF EXISTS `" + table_name + "`;")
        except pymysql.err.DatabaseError as e:
            Writer.error("Critical error working with database:", e)
            exit()
        else:
            self.conn.commit()
            Writer.action_with_highlight("Table `", table_name, "` has been dropped.")

    def close_connections(self):
        try:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except pymysql.err.DatabaseError as e:
            Writer.error("Critical error closing database connection:", e)
            exit()
        else:
            Writer.action("Database connection closed.")

    def add_set(self, set):
        self.query("INSERT INTO sets (name, code, releaseDate, border, type, onlineOnly) VALUES ( " +
                    "'" + (set['name'].replace("'", "''")).replace("—", "-") + "', " +
                    "'" + set['code'] + "', " +
                    "'" + set['releaseDate'] + "', " +
                    "'" + set['border'] + "', " +
                    "'" + set['type'] + "', " +
                    ('1' if set['onlineOnly'] is True else '0') + ");")

    def add_card(self, card, set):
        Translator = translator_service.TranslatorService(card)
        self.query("INSERT INTO cards (name, manaCost, cmc, `set`, rarity, text, flavor, artist, number, power, "
                   "toughness, loyalty, multiverseid, watermark, border, layout, timeshifted, reserved, starter) "
                   "VALUES (" +
                   Translator.db['name'] + ", " +
                   Translator.db['manaCost'] + ", " +
                   Translator.db['cmc'] + ", " +
                   set + ", " +
                   Translator.db['rarity'] + ", " +
                   Translator.db['text'] + ", " +
                   Translator.db['flavor'] + ", " +
                   Translator.db['artist'] + ", " +
                   Translator.db['number'] + ", " +
                   Translator.db['power'] + ", " +
                   Translator.db['toughness'] + ", " +
                   Translator.db['loyalty'] + ", " +
                   Translator.db['multiverseid'] + ", " +
                   Translator.db['watermark'] + ", " +
                   Translator.db['border'] + ", " +
                   Translator.db['layout'] + ", " +
                   Translator.db['timeshifted'] + ", " +
                   Translator.db['reserved'] + ", " +
                   Translator.db['starter'] +
                   ");")

    def build_database(self, data_cards, data_sets):
        for table in self.tables:
            self.drop_table(table)
            self.create_table(table)
        i, j = 0, 0
        variant_builder = []
        multiverse_map = {}
        for set in data_sets:
            i += 1
            self.add_set(set)
            for card in data_cards[set['code']]["cards"]:
                j += 1
                self.add_card(card, str(i))
                Translator = translator_service.TranslatorService(card)
                if Translator.db['names']:
                    for name in Translator.db['names']:
                        self.query("INSERT INTO names (card, name) VALUES (" + str(j) + ", " + name + ");")
                if Translator.db['colors']:
                    for color in Translator.db['colors']:
                        self.query("INSERT INTO colors (card_id, color) VALUES (" + str(j) + ", " + color + ");")
                if Translator.db['colorIdentities']:
                    for colorIdentity in Translator.db['colorIdentities']:
                        self.query("INSERT INTO color_identities (card_id, color) VALUES ("
                                   + str(j) + ", " + colorIdentity + ");")
                if Translator.db['supertypes']:
                    for supertype in Translator.db['supertypes']:
                        self.query("INSERT INTO supertypes (card_id, supertype) VALUES ("
                                   + str(j) + ", " + supertype + ");")
                if Translator.db['types']:
                    for type in Translator.db['types']:
                        self.query("INSERT INTO types (card_id, type) VALUES (" + str(j) + ", " + type + ");")
                if Translator.db['subtypes']:
                    for subtype in Translator.db['subtypes']:
                        self.query("INSERT INTO subtypes (card_id, subtype) VALUES (" + str(j) + ", " + subtype + ");")
                if Translator.db['variations']:
                    for variant in Translator.db['variations']:
                        variant_builder.append([j, int(variant)])
                if 'multiverseid' in card:
                    multiverse_map[card['multiverseid']] = j
            Writer.action_with_highlight(Writer.progress(i, 223) + "Synchronized ", set['name'], ".")

        for item in variant_builder:
            self.query(
                "INSERT INTO variations (card_id, variant_id) VALUES (" + str(item[0]) + ", " +
                str(multiverse_map[item[1]]) + ");")
        self.close_connections()
