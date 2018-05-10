import pymysql
import database.identity
import card_formatter
from writer_service import Writer


class DatabaseService(object):
    tables = ['cards']

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

    def create_table(self, table_name):
        if table_name == "cards":
            try:
                self.cur.execute("""CREATE TABLE `cards` (
                                  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT, 
                                  `name` varchar(33) NOT NULL,
                                  `names` varchar(100) DEFAULT NULL,
                                  `manaCost` varchar(45) DEFAULT NULL,
                                  `cmc` int(11) DEFAULT NULL,
                                  `set` varchar(10) NOT NULL,
                                  `colors` varchar(45) NOT NULL,
                                  `colorIdentity` varchar(45) NOT NULL,
                                  `type` varchar(50) NOT NULL,
                                  `supertypes` varchar(15) DEFAULT NULL,
                                  PRIMARY KEY (`id`)
                                  ) ENGINE=InnoDB AUTO_INCREMENT=32677 DEFAULT CHARSET=utf8;""")
            except pymysql.err.DatabaseError as e:
                Writer.error("Critical error working with database:", e)
                exit()
            else:
                self.conn.commit()
                Writer.action_with_highlight("Table `", table_name, "` has been created.")

    def wipe_table(self, table_name):
        try:
            self.cur.execute("TRUNCATE TABLE `" + table_name + "`;")
            self.cur.execute("ALTER TABLE `cards` AUTO_INCREMENT = 1;")
        except pymysql.err.DatabaseError as e:
            Writer.error("Critical error working with database:", e)
            exit()
        else:
            self.conn.commit()
            Writer.action_with_highlight("Table `", table_name, "` has been wiped.")

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

    def add_card(self, name, names, mana_cost, cmc, set, colors, color_identity, type, supertypes):
        self.cur.execute("INSERT INTO cards (name, names, manaCost, cmc, `set`, colors, colorIdentity, type, supertypes) VALUES (" +
                         name + ", " + names + ", " + mana_cost + ", " + cmc + ", " + set + ", " + colors + ", " +
                         color_identity + ", " + type + ", " + supertypes + ");")

    def check_table_exists(self, table_name):
        self.cur.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_name =  '""" + table_name + """'""" )
        if self.cur.fetchone()[0] == 1:
            return True
        return False

    def build_database(self, sets, data):
        for table in self.tables:
            if self.check_table_exists(table):
                self.wipe_table(table)
            else:
                self.create_table(table)
        i = 0
        for set in sets:
            i += 1
            for card in data[set]["cards"]:
                Formatter = card_formatter.CardFormatter(card)
                # Writer.display_card(card, set)
                self.add_card(
                    Formatter.name_for_db(),
                    Formatter.names_for_db(),
                    Formatter.mana_cost_for_db(),
                    Formatter.cmc_for_db(),
                    "'" + set + "'",
                    Formatter.colors_for_db(),
                    Formatter.color_identity_for_db(),
                    Formatter.type_for_db(),
                    Formatter.supertypes_for_db()
                )
            Writer.action_with_highlight(Writer.progress(i, len(sets)) + "Synchronized ", set, ".")
        self.close_connections()