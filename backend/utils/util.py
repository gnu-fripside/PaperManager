# encoding:utf-8
from .TagTree import TagTree
from .ArxivScrapy import paperDown
from .PaperNode import PaperNode
from backend.models import *
import os
import time
import shutil
import zipfile


def AddPaper(userid, title, author, time, tags, source, filePath):
    pass

def UpdatePaperInfo(userid):
    pass

"""
function movePaper(userid, paperNode, newTag):
    str userid: the user's name
    PaperNode paperNode: tag needs to be added
    str newTag:new Tag path of this paper, separated by point
    :return
        PaperNode paperNode: new PaperNode object, with updated information
"""

def movePaper(userid, paperNode, newTag):
    newPath = "../resource/tags/"+str(userid)+"/"+"/".join(newTag.split("."))+paperNode["filePath"].split("/")[-1]
    shutil.copyfile(paperNode["filePath"],newPath)
    os.remove(paperNode["filePath"])
    paperNode["filePath"] = newPath
    paperNode["tags"] = newTag
    return paperNode

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
    rootDir = "../resource/tags/" + str(userid) + "/"
    targetPath = rootDir + os.path.join(parentTag.split(".").append(tag))
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
        return {'error_num':0,'message':"create succeed."}
    else:
        return {'error_num':1,'message':"exists"}
    
"""
function getTagList(userid, currentPath):
    str userid: the user's name
    str currentPath: the current tag path, separated by point
    :return
        dict result: search result
        :parameter
            int error_num: return error code, 0, means succeed, 1 means no sub tag, 2 means current tag not exist
            str msg: message
            list tagList: son tags
"""

def getTagList(userid, currentPath):
    result = {}
    rootDir = "../resource/tags/" + userid + "/"
    rootDir += "/".join(currentPath.split("."))
    print('rootDir: ' + rootDir)
    try:
        sonDir = os.listdir(rootDir)
        sonDir = [item for item in sonDir if item[-5:] != '.json']
        print(sonDir)
    except FileNotFoundError:
        result['error_num'] = 2
        result['msg'] = "fail, no such directory"
        result['tagList'] = []
        return result
    try:
        sonDir.remove('.DS_Store')
    except:
        pass
    len_sonDir = len(sonDir)
    if len_sonDir <= 0:
        result['error_num'] = 1
        result['msg'] = "fail, no son directory exists"
        result['tagList'] = []
    else:
        result['error_num'] = 0
        result['msg'] = "success"
        result['tagList'] = sonDir
    return result


def getFileList(userid, currentPath):
    result = {}
    rootDir = "../resource/tags/" + userid + "/"
    rootDir += "/".join(currentPath.split("."))
    try:
        sonDir = os.listdir(rootDir)
    except FileNotFoundError:
        result['error_num'] = 2
        result['msg'] = "fail, no such directory"
        result['fileList'] = []
        return result
    try:
        sonDir.remove('.DS_Store')
    except:
        pass
    sonFile = []
    for son in sonDir:
        if os.path.isfile(rootDir + "/" + son):
            sonFile.append(son.split(".")[0])
    len_sonFile = len(sonFile)
    if len_sonFile <= 0:
        result['error_num'] = 1
        result['msg'] = "fail, no paper in this tag"
        result['fileList'] = []
    else:
        result['error_num'] = 0
        result['msg'] = "success"
        result['fileList'] = sonFile
    return result

def PaperNodePack(paper_node, userid, tempDir, outputDir, note, log):
    path = os.path.join(tempDir, str(userid))
    if not os.path.exists(path):
        os.makedirs(path)
    note_path = os.path.join(path, "note.json")
    log_path = os.path.join(path, "log.json")
    shutil.copy(paper_node.filePath, os.path.join(path, paper_node.hash + ".pdf"))
    info_path = os.path.join(path, "info.json")
    with open(info_path,"w") as f:
        f.write(str(paper_node.toDict()))
        f.close()
    with open(note_path, "w") as f:
        f.write(str(note))
        f.close()
    with open(log_path, "w") as f:
        f.write(str(log))
        f.close()
    outputPath = os.path.join(outputDir, str(userid)+"_"+str(int(time.time())) + ".zip")
    with zipfile.ZipFile(outputPath, "w",
                         zipfile.ZIP_DEFLATED) as f:
        for dirPath, dirNames, fileNames in os.walk(path):
            for filename in fileNames:
                f.write(os.path.join(dirPath, filename))
        f.close()
    shutil.rmtree(path)
    return outputPath

def FindPaperNote(username, paperNode):
    notes = Note.objects.filter(username=username, paper_title=paperNode.title)
    note_dict = []
    for note in notes:
        tmp = {'page': note.paper_page, 'content': note.content}
        note_dict.append(tmp)
    return note_dict

def FindPaperLog(username, paperNode):
    logs = Log.objects.filter(username=username, paper_title=paperNode.title)
    log_dict = []
    for log in logs:
        tmp = {'log_id': log.id, 'log_content': log.log}
        log_dict.append(tmp)
    return log_dict

def SubTreePack(subtreePath, userid, tempDir, outputDir):
    piece = "/".join(subtreePath.split("."))
    originPath = "../resource/tags/" + userid + piece
    tempRoot = os.path.join(tempDir,userid)
    tempPath = os.path.join(tempRoot, piece)
    shutil.copytree(originPath, tempPath)
    outputPath = os.path.join(outputDir, str(userid) + "_" + str(int(time.time())) + ".zip")
    with zipfile.ZipFile(outputPath, "w",
                         zipfile.ZIP_DEFLATED) as f:
        for dirPath, dirNames, fileNames in os.walk(tempRoot):
            for filename in fileNames:
                f.write(os.path.join(dirPath, filename))
        f.close()
    shutil.rmtree(tempRoot)
    return outputPath
    pass

if __name__ == "__main__":
    #print(getTagList("10010", "manga.lovelive"))
    #print(getTagList("10010", "manga.ddlc"))
    #print(getTagList("10010", "manga.white_album"))
    print(getTagList("10032","cs.ai"))
    print(getTagList("10032", "cs.se"))
    print(getTagList("10032", "cs"))
    print(getTagList("10033", "cs"))

