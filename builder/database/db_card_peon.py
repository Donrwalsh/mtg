import pymysql
import database.identity


class DbCardPeon(object):

    def __init__(self):
        self.conn = pymysql.connect(host=database.identity.host,
                                    user=database.identity.user,
                                    passwd=database.identity.passwd,
                                    db=database.identity.db)
        self.cur = self.conn.cursor()

    def reset_table(self, tableName):
        self.cur.execute("TRUNCATE TABLE `" + tableName + "`;")
        self.cur.execute("ALTER TABLE `cards` AUTO_INCREMENT = 1;")

    def close_connections(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def add_card(self, name):
        self.cur.execute("INSERT INTO cards (name) VALUES ('" + name.replace("'", "''") + "');")