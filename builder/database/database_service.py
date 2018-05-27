import pymysql
import database.identity
from writer_service import Writer
import translator_service


class DatabaseService(object):

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
                                      `card_id` int(11) unsigned NOT NULL,
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
        # Writer.action_with_highlight("Table `", table_name, "` has been created.")

    def drop_table(self, table_name):
        try:
            self.cur.execute("DROP TABLE IF EXISTS `" + table_name + "`;")
        except pymysql.err.DatabaseError as e:
            Writer.error("Critical error working with database:", e)
            exit()
        else:
            self.conn.commit()
            # Writer.action_with_highlight("Table `", table_name, "` has been dropped.")

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

    def add_card(self, translated_card, set):
        self.query("INSERT INTO cards (name, manaCost, cmc, `set`, rarity, text, flavor, artist, number, power, "
                   "toughness, loyalty, multiverseid, watermark, border, layout, timeshifted, reserved, starter) "
                   "VALUES (" +
                   translated_card.db['name'] + ", " +
                   translated_card.db['manaCost'] + ", " +
                   translated_card.db['cmc'] + ", " +
                   set + ", " +
                   translated_card.db['rarity'] + ", " +
                   translated_card.db['text'] + ", " +
                   translated_card.db['flavor'] + ", " +
                   translated_card.db['artist'] + ", " +
                   translated_card.db['number'] + ", " +
                   translated_card.db['power'] + ", " +
                   translated_card.db['toughness'] + ", " +
                   translated_card.db['loyalty'] + ", " +
                   translated_card.db['multiverseid'] + ", " +
                   translated_card.db['watermark'] + ", " +
                   translated_card.db['border'] + ", " +
                   translated_card.db['layout'] + ", " +
                   translated_card.db['timeshifted'] + ", " +
                   translated_card.db['reserved'] + ", " +
                   translated_card.db['starter'] +
                   ");")

    def populate_normalized_table(self, translated_card, id, field):
        table_name = field if field != 'colorIdentities' else 'color_identities'
        column_names = {
            'names': 'name',
            'colors': 'color',
            'colorIdentities': 'color',
            'supertypes': 'supertype',
            'types': 'type',
            'subtypes': 'subtype',
        }
        if translated_card.db[field]:
            for item in translated_card.db[field]:
                self.query("INSERT INTO " + table_name + "(card_id, " + column_names[field] +
                           ") VALUES (" + id + ", " + item + ");")

    def build_database(self, data_cards, data_sets):
        tables = ('cards', 'names', 'sets', 'colors', 'color_identities', 'supertypes', 'types', 'subtypes', 'variations')
        Writer.action_stub("Dropping tables ")
        for table in tables:
            Writer.action_with_highlight_stub("`", table, "` " if table != 'variations' else "`")
            self.drop_table(table)
        Writer.action('.')
        Writer.action_stub("Creating tables ")
        for table in tables:
            Writer.action_with_highlight_stub("`", table, "` " if table != 'variations' else "`")
            self.create_table(table)
        Writer.action('.')

        variant_builder = {}
        i, j = 0, 0
        for s_index, set in enumerate(data_sets):
            self.add_set(set)
            for card in data_cards[set['code']]["cards"]:
                i += 1
                translated_card = translator_service.TranslatorService(card)
                self.add_card(translated_card, str(s_index+1))
                for field in ("names", "colors", 'colorIdentities', 'supertypes', 'types', 'subtypes'):
                    self.populate_normalized_table(translated_card, str(i), field)
                if card['name'] not in variant_builder:
                    variant_builder[card['name']] = [i]
                else:
                    for variant in variant_builder[card['name']]:
                        self.query(
                            "INSERT INTO variations (card_id, variant_id) VALUES (" + str(variant) + ", " +
                            str(i) + ");")
                        self.query(
                            "INSERT INTO variations (card_id, variant_id) VALUES (" + str(i) + ", " +
                            str(variant) + ");")
                    variant_builder[card['name']].append(i)
            Writer.action_with_highlight_stub(Writer.progress(s_index, len(data_sets)) + " Synchronized ", set['name'.replace('—', '-')], Writer.pad_right(".", 42-len(set['name'])))
            Writer.action_with_highlight('| ', Writer.pad_right(str(i - j), 3), ' | ')
            j = i
        self.close_connections()
