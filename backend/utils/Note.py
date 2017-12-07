#encoding:utf-8

class Note:
	def __init__(self, paper_title, username, paper_page, content):
		self.paper_title = paper_title
		self.username = username
		self.paper_page = paper_page
		self.content = content
	
	def toDict(self):
		noteDict = {}
		noteDict["paper_title"] = self.paper_page
		noteDict["username"] = self.username
		noteDict["paper_page"] = self.paper_page
		noteDict["content"] = self.content
		return noteDict
