from model.data_source import DataSource
import pymysql
import identity
from writer_service import Writer


class DatabaseService(DataSource):

    def __init__(self, **kwargs):
        try:
            self.conn = pymysql.connect(host=identity.host,
                                        user=identity.user,
                                        passwd=identity.passwd,
                                        db=identity.db,
                                        cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.conn.cursor()
        except pymysql.err.DatabaseError as e:
            # Writer.error("Critical error connecting to database", e)
            exit()
        else:
            pass
            # Writer.action("Connected to database.")
        self.conn.set_charset('utf8')

        DataSource.__init__(self, "Database")

    def sets_initiate(self):
        self.cur.execute("SELECT * FROM sets")
        Writer.action(Writer.pad_right("", 13))
        return self.cur.fetchall()

