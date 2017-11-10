#encoding:utf-8
from utils.TagTree import TagTree
from utils.ArxivScrapy import paperDown
from utils.PaperNode import PaperNode

def AddPaper():
    pass

def initializeTagTree(userid, filePath):
    rootTag = TagTree("root", userid, None)
    with open(filePath, "w") as f:
        f.write(str(rootTag.toDict()))
        f.close()
    return rootTag

def AddTag(tag, parentTag):
    pass


