import os
from writer_service import Writer

class DataSource(object):

    def __init__(self, name, **kwargs):
        self.name = name
        self.update = kwargs.get('update')

        Writer.action(Writer.pad_right(self.name, 13))
        self.sets = self.sets_initiate()
        Writer.highlight(len(self.sets))

        Writer.newline()

    def sets_initiate(self):
        pass

    def set_by_code(self, code):
        return next(item for item in self.sets if item['code'] == code)