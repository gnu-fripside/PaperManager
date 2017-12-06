#encoding:utf-8

class Log:
	def __init__(self, username, log):
		self.username = username
		self.log = log
	def toDict(self):
		logDict = {}
		logDict["username"] = self.username
		logDict["log"] = self.log
		return logDict
