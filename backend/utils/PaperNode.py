import os
import hashlib
import shutil
import zipfile
"""
class PaperNode:
    str userid: the symbol of user
    str title: paper's title
    list(str) author: author of this paper
    str publishtime: paper's publish time
    str addtime: paper's add time
    list(str) tags: tags of this paper, edited by each user, from root to leaf
    str source: the conference or periodical of this paper
    str url: online read link of this paper, can be None
    dict notes: notes add by user
    str filePath: the path of origin file
    str hash: sha1 value of the origin file
    int readStatus: read status of this paper, 0 means not read, 1 means roughly, 2 means clearly
    method AddNote

    method toDict():
        return: dict dictPaperNode: paper info in dict type

    method Pack(userid, tempDir, outputDir):
        not complete!!!
        :parameter
            str userid: the symbol of user
            str tempDir: path of temp directory
            str outputDir: path of output directory, store the formatted file
        :return
            str outputPath: the path of formatted file
"""


class PaperNode:
    def __init__(self, userid, title, author, publishtime, addtime, tags, source, url, filePath, readStatus):
        self.userid = userid
        self.title = title
        self.author = author
        self.publishtime = publishtime
        self.addtime = addtime
        self.tags = tags
        self.source = source
        self.url = url
        self.filePath = filePath
        self.readStatus = readStatus
        with open(self.filePath, "rb") as f:
            sha1obj = hashlib.sha1()
            sha1obj.update(f.read())
            self.hash = str(sha1obj.hexdigest())
            f.close()

    def toDict(self):
        dictPaperNode = {}
        dictPaperNode["title"] = self.title
        dictPaperNode["author"] = self.author
        dictPaperNode["publishtime"] = str(self.time)
        dictPaperNode["addtime"] = str(self.addtime)
        dictPaperNode["tags"] = []
        for i in range(len(self.tags)):
            dictPaperNode["tags"][str(i + 1)] = self.tags[i]
        dictPaperNode["source"] = self.source
        dictPaperNode["url"] = self.url
        dictPaperNode["filePath"] = self.filePath
        dictPaperNode["hash"] = self.hash
        dictPaperNode["readStatus"] = self.readStatus
        return dictPaperNode

    def Pack(self, userid, tempDir, outputDir):
        path = os.path.join(tempDir, str(userid) + "_" + self.hash)
        notePath = os.path.join(path, "noteFile")
        logPath = os.path.join(path, "logFile")
        os.makedirs(path)
        os.makedirs(notePath)
        shutil.copy(self.filePath, os.path.join(tempDir, self.hash + ".pdf"))
        noteKeys = self.notes.keys()
        for i in range(len(noteKeys)):
            shutil.copy(self.notes[noteKeys[i]], os.path.join())
        with zipfile.ZipFile(os.path.join(outputDir, str(userid) + "_" + self.hash + ".zip"), "w", zipfile.ZIP_DEFLATED) as f:
            for dirPath, dirNames, fileNames in os.walk(path):
                for filename in fileNames:
                    f.write(os.path.join(dirPath, filename))
            f.close()
        shutil.rmtree(path)
        return os.path.join(outputDir, str(userid) + "_" + self.hash + ".zip")
