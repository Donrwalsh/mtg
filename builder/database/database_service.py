import pymysql
import database.identity
import card_formatter
from writer_service import Writer


class DatabaseService(object):
    tables = ('cards', 'names', 'sets', 'colors')

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

    def query(self, query):
        try:
            self.cur.execute(query)
        except pymysql.err.DatabaseError as e:
            Writer.SQL_error("Critical error working with database:", e, query)
            exit()

    def create_table(self, table_name):
        if table_name == 'cards':
            self.query("""CREATE TABLE `cards` (
                                      `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT, 
                                      `name` varchar(150) NOT NULL,
                                      `manaCost` varchar(45) DEFAULT NULL,
                                      `cmc` int(11) DEFAULT NULL,
                                      `set` int(11) NOT NULL,
                                      `colorIdentity` varchar(45) NOT NULL,
                                      `type` varchar(50) NOT NULL,
                                      `supertypes` varchar(15) DEFAULT NULL,
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
        onlineOnly = '1' if set['onlineOnly'] is True else '0'
        self.query("INSERT INTO sets (name, code, releaseDate, border, type, onlineOnly) VALUES ( " +
                         "'" + (set['name'].replace("'", "''")).replace("—", "-") + "', " +
                         "'" + set['code'] + "', " +
                         "'" + set['releaseDate'] + "', " +
                         "'" + set['border'] + "', " +
                         "'" + set['type'] + "', " +
                         onlineOnly + ");")

    def add_card(self, card, set):
        Formatter = card_formatter.CardFormatter(card)
        self.query("INSERT INTO cards (name, manaCost, cmc, `set`, colorIdentity, type, supertypes) VALUES (" +
                         Formatter.name_for_db() + ", " +
                         Formatter.mana_cost_for_db() + ", " +
                         Formatter.cmc_for_db() + ", " +
                         set + ", " +
                         Formatter.color_identity_for_db() + ", " +
                         Formatter.type_for_db() + ", " +
                         Formatter.supertypes_for_db() +
                         ");")

    def build_database(self, sets, data, set_data):
        for table in self.tables:
            self.drop_table(table)
            self.create_table(table)
        i, j = 0, 0
        for set in set_data:
            i += 1
            self.add_set(set)
            for card in data[set['code']]["cards"]:
                j += 1
                self.add_card(card, str(i))
                if 'names' in card:
                    for name in card['names']:
                        # self.add_names(i, name)
                        self.query(
                            "INSERT INTO names (card, name) VALUES (" +
                            str(j) + ", '" + name.replace("'", "''") + "');")
                if 'colors' in card:
                    for color in card['colors']:
                        self.query(
                            "INSERT INTO colors (card_id, color) VALUES (" +
                            str(j) + ", '" + color + "');")
                else:
                    self.query(
                        "INSERT INTO colors (card_id, color) VALUES (" +
                        str(j) + ", 'Colorless');")
            Writer.action_with_highlight(Writer.progress(i, 223) + "Synchronized ", set['name'], ".")
        self.close_connections()