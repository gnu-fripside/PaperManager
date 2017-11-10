#encoding:utf-8
from utils.TagTree import TagTree
from utils.ArxivScrapy import paperDown
from utils.PaperNode import PaperNode

def AddPaper(userid, title, author, time, tags, source, filePath):
    pass

def initializeTagTree(userid, filePath):
    rootTag = TagTree("root", userid, None)
    with open(filePath, "w") as f:
        f.write(str(rootTag.toDict()))
        f.close()
    return rootTag
"""
function AddTag(userid, tag, parentTag)
    str userid: the symbol of TagTree
    str tag: tag needs to be added
    list parentTag: parent tags, from root to direct parent of new tag
"""
def AddTag(userid, tag, parentTag):
    pass


