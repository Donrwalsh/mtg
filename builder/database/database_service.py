import pymysql
import database.identity
import card_formatter
from writer_service import Writer


class DatabaseService(object):
    tables = ('cards', 'names', 'sets')

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
                                  `name` varchar(150) NOT NULL,
                                  `manaCost` varchar(45) DEFAULT NULL,
                                  `cmc` int(11) DEFAULT NULL,
                                  `set` int(11) NOT NULL,
                                  `colors` varchar(45) NOT NULL,
                                  `colorIdentity` varchar(45) NOT NULL,
                                  `type` varchar(50) NOT NULL,
                                  `supertypes` varchar(15) DEFAULT NULL,
                                  PRIMARY KEY (`id`)
                                  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;""")
            except pymysql.err.DatabaseError as e:
                Writer.error("Critical error working with database:", e)
                exit()
        elif table_name == "names":
            try:
                self.cur.execute("""CREATE TABLE `names` (
                                  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                  `card` int(11) unsigned NOT NULL,
                                  `name` VARCHAR(50) NOT NULL,
                                  PRIMARY KEY (`id`)
                                  ) ENGINE=InnoDB DEFAULT CHARSET=utf8; """)
            except pymysql.err.DatabaseError as e:
                Writer.error("Critical error working with database:", e)
                exit()
        elif table_name == "sets":
            try:
                self.cur.execute("""CREATE TABLE `sets` (
                                  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                                  `name` VARCHAR(50) NOT NULL,
                                  `code` VARCHAR(10) NOT NULL,
                                  `releaseDate` DATE NOT NULL,
                                  `border` VARCHAR(50) NOT NULL,
                                  `type` VARCHAR(50) NOT NULL,
                                  `onlineOnly` TINYINT(1) NOT NULL,
                                  PRIMARY KEY (`id`)
                                  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
            except pymysql.err.DatabaseError as e:
                Writer.error("Critical error working with database:", e)
                exit()
        self.conn.commit()
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

    # def wipe_table(self, table_name):
    #     try:
    #         self.cur.execute("TRUNCATE TABLE `" + table_name + "`;")
    #         self.cur.execute("ALTER TABLE `cards` AUTO_INCREMENT = 1;")
    #     except pymysql.err.DatabaseError as e:
    #         Writer.error("Critical error working with database:", e)
    #         exit()
    #     else:
    #         self.conn.commit()
    #         Writer.action_with_highlight("Table `", table_name, "` has been wiped.")

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

    def add_set(self, name, code, releaseDate, border, type, onlineOnly):
        self.cur.execute("INSERT INTO sets (name, code, releaseDate, border, type, onlineOnly) VALUES (" +
                         name + ", " + code + ", " + releaseDate + ", " + border + ", " + type + ", " +
                         onlineOnly + ");")

    def add_card(self, name, mana_cost, cmc, set, colors, color_identity, type, supertypes):
        print("INSERT INTO cards (name, manaCost, cmc, `set`, colors, colorIdentity, type, supertypes) VALUES (" +
                         name + ", " + mana_cost + ", " + cmc + ", " + set + ", " + colors + ", " +
                         color_identity + ", " + type + ", " + supertypes + ");")
        self.cur.execute("INSERT INTO cards (name, manaCost, cmc, `set`, colors, colorIdentity, type, supertypes) VALUES (" +
                         name + ", " + mana_cost + ", " + cmc + ", " + set + ", " + colors + ", " +
                         color_identity + ", " + type + ", " + supertypes + ");")

    def check_table_exists(self, table_name):
        self.cur.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_name =  '""" + table_name + """'""" )
        if self.cur.fetchone()[0] == 1:
            return True
        return False

    def build_database(self, sets, data, set_data):
        for table in self.tables:
            self.drop_table(table)
            self.create_table(table)
        i = 0
        j = 0
        for set in set_data:
            i += 1
            self.add_set(
                "'" + (set['name'].replace("'", "''")).replace("—", "-") + "'",
                "'" + set['code'] + "'",
                "'" + set['releaseDate'] + "'",
                "'" + set['border'] + "'",
                "'" + set['type'] + "'",
                '1' if set['onlineOnly'] is True else '0'
            )
            for card in data[set['code']]["cards"]:
                j += 1
                Formatter = card_formatter.CardFormatter(card)
                # print(Formatter.db)
                self.add_card(
                    Formatter.name_for_db(),
                    Formatter.mana_cost_for_db(),
                    Formatter.cmc_for_db(),
                    str(i),
                    Formatter.colors_for_db(),
                    Formatter.color_identity_for_db(),
                    Formatter.type_for_db(),
                    Formatter.supertypes_for_db()
                )
                if 'names' in card:
                    for name in card['names']:
                        # self.add_names(i, name)
                        self.cur.execute(
                            "INSERT INTO names (card, name) VALUES (" +
                            str(j) + ", '" + name.replace("'", "''") + "');")
            Writer.action_with_highlight(Writer.progress(i, 223) + "Synchronized ", set['name'], ".")
        self.close_connections()