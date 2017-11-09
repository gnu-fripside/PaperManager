import os

class PaperNode:
    def __init__(self, title, author, time, tags, source, filePath):
        self.title = title
        self.author = author
        self.time = time
        self.tags = tags
        self.source = source
        self.notes = None
        self.filePath = filePath
    def AddNote(self):
        pass
    def Pack(self):
        pass
