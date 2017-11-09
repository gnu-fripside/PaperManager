#encoding:utf-8
import os
import sys

class Category:
    def __init__(self, name, id, father):
        self.name = name
        self.id = id
        self.father = father
        self.son = []
