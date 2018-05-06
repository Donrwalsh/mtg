import pymysql
import database.identity
from colorama import Fore
from colorama import Style


class DbCardPeon(object):

    def __init__(self):
        try:
            self.conn = pymysql.connect(host=database.identity.host,
                                        user=database.identity.user,
                                        passwd=database.identity.passwd,
                                        db=database.identity.db)
            self.cur = self.conn.cursor()
        except pymysql.err.DatabaseError as e:
            print(f"{Fore.LIGHTRED_EX}Critical error connecting to database: \n" + str(e))
            exit()
        else:
            print(f"{Fore.BLUE}Connected to database.{Style.RESET_ALL}")

    def reset_table(self, tableName):
        try:
            self.cur.execute("TRUNCATE TABLE `" + tableName + "`;")
            self.cur.execute("ALTER TABLE `cards` AUTO_INCREMENT = 1;")
        except pymysql.err.DatabaseError as e:
            print(f"{Fore.LIGHTRED_EX}Critical error working with database: \n" + str(e))
            exit()
        else:
            print(f"{Fore.BLUE}Table {Fore.YELLOW}`" + tableName + f"`{Fore.BLUE} has been wiped.{Style.RESET_ALL}")

    def close_connections(self):
        try:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except pymysql.err.DatabaseError as e:
            print(f"{Fore.LIGHTRED_EX}Critical error finalizing database changes: \n" + str(e))
            exit()
        else:
            print(f"{Fore.BLUE}Database changes finalized.{Style.RESET_ALL}")

    def add_card(self, name, names, manaCost, cmc, set, colors, colorIdentity):
        self.cur.execute("INSERT INTO cards (name, names, manaCost, cmc, `set`, colors, colorIdentity) VALUES (" +
                         name + ", " + names + ", " + manaCost + ", " + str(cmc) + ", " +
                         set + ", " + colors + ", " + colorIdentity + ");")