from model.data_source import DataSource
import pymysql
import identity
from writer_service import Writer
from model.database_tables import *
from helper_service import Helper


class Database(DataSource):

    def __init__(self):
        try:
            self.conn = pymysql.connect(host=identity.host,
                                        user=identity.user,
                                        passwd=identity.passwd,
                                        db=identity.db,
                                        cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.conn.cursor()
        except pymysql.err.DatabaseError as e:
            Writer.error("\nCritical error connecting to database", e)
            exit()
        else:
            pass
            # Writer.action("Connected to database.")
        self.conn.set_charset('utf8')

        DataSource.__init__(self, "Database")

    def sets_initiate(self):
        try:
            self.cur.execute("SELECT * FROM sets")
            Writer.option(Writer.pad_right(" [exists]", 13))
        except pymysql.err.ProgrammingError:
            Writer.option(Writer.pad_right(" [created]", 13))
            self.build_sets_table()
        return self.cur.fetchall()

    def build_sets_table(self):
        self.query(SETS)

    def add_set(self, sets):
        self.query(SETS_INSERT +
              Helper.select_for_query(sets, 'code') + ", "
                   + Helper.select_for_query(sets, 'name') + ", "
                   + Helper.select_for_query(sets, 'set_type') + ", "
                   + Helper.select_for_query(sets, 'released_at') + ", "
                   + Helper.select_for_query(sets, 'block') + ", "
                   + Helper.select_for_query(sets, 'block_code') + ", "
                   + Helper.select_for_query(sets, 'parent_set_code') + ", "
                   + Helper.select_for_query(sets, 'card_count') + ", "
                   + Helper.select_for_query(sets, 'border')
                   + ");")


    def query(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except pymysql.err.DatabaseError as e:
            Writer.SQL_error("Critical error working with database:", e, query)
            exit()
        except UnicodeEncodeError as e:
            Writer.SQL_error("Critical encoding error:", e, query)
            exit()

    def set_by_code(self, code):
        return next(item for item in self.sets if item['code'] == code)