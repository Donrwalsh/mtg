import pymysql
import database.identity

from writer_service import Writer


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

    def wipe_table(self, table_name):
        try:
            self.cur.execute("TRUNCATE TABLE `" + table_name + "`;")
            self.cur.execute("ALTER TABLE `cards` AUTO_INCREMENT = 1;")
        except pymysql.err.DatabaseError as e:
            Writer.error("Critical error working with database:", e)
            exit()
        else:
            Writer.action_with_highlight("Table `", table_name, "` has been wiped.")

    def close_connections(self):
        try:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except pymysql.err.DatabaseError as e:
            Writer.error("Critical error finalizing database changes:", e)
            exit()
        else:
            Writer.action("Database changes finalized.")

    def add_card(self, name, names, mana_cost, cmc, set, colors, color_identity):
        self.cur.execute("INSERT INTO cards (name, names, manaCost, cmc, `set`, colors, colorIdentity) VALUES (" +
                         name + ", " + names + ", " + mana_cost + ", " + str(cmc) + ", " +
                         set + ", " + colors + ", " + color_identity + ");")