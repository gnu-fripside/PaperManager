import os
import hashlib
import shutil
import zipfile
"""
str title: paper's title
str time: 
"""
class PaperNode:
    def __init__(self, title, author, time, tags, source, filePath):
        self.title = title
        self.author = author
        self.time = time
        self.tags = tags
        self.source = source
        self.notes = {}
        self.filePath = filePath
        with open(self.filePath,"rb") as f:
            sha1obj = hashlib.sha1()
            sha1obj.update(f.read())
            self.hash = str(sha1obj.hexdigest())
            f.close()

    def AddNote(self):
        pass

    def toDict(self):
        dictPaperNode = {}
        dictPaperNode["title"] = self.title
        dictPaperNode["author"] = self.author
        dictPaperNode["time"] = str(self.time)
        dictPaperNode["tags"] = {}
        for i in range(len(self.tags)):
            dictPaperNode["tags"][str(i+1)] = self.tags[i]
        dictPaperNode["sourxe"] = self.source
        dictPaperNode["notes"] = self.notes
        dictPaperNode["filePath"] = self.filePath
        dictPaperNode["hash"] = self.hash
        return dictPaperNode

    def Pack(self, userid, tempDir, outputDir):
        path = os.path.join(tempDir, str(userid)+"_"+self.hash)
        notePath = os.path.join(path, "noteFile")
        os.makedirs(path)
        os.makedirs(notePath)
        shutil.copy(self.filePath, os.path.join(tempDir, self.hash+".pdf"))
        noteKeys = self.notes.keys()
        for i in range(len(noteKeys)):
            shutil.copy(self.notes[noteKeys[i]], os.path.join())
        with zipfile.ZipFile(os.path.join(tempDir, str(userid)+"_"+self.hash+".zip"),"w",zipfile.ZIP_DEFLATED) as f:
            for dirPath, dirNames, fileNames in os.walk(path):
                for filename in fileNames:
                    f.write(os.path.join(dirPath,filename))
            f.close()
        return os.path.join(tempDir, str(userid)+"_"+self.hash+".zip")
