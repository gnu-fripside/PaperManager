# encoding:utf-8
import os
import sys


class TagTree:
    def __init__(self, name, userid, father):
        self.name = name
        self.userid = userid
        self.father = father
        self.son = []

    def toDict(self):
        dictTagTree = {}
        dictTagTree["name"] = self.name
        dictTagTree["userid"] = str(self.userid)
        dictTagTree["father"] = str(self.father)
        dictTagTree["son"] = {}
        for i in range(len(self.son)):
            dictTagTree["son"][str(i + 1)] = self.son[i]
        return dictTagTree
