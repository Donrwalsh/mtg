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

