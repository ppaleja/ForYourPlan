from PrereqScraper import getPrereqs

class Course:
  def __init__(self, code, name, fTeacher, wTeacher, sTeacher):
		self.code = code
		self.name = name
		self.fTeacher = fTeacher
		self.wTeacher = wTeacher
		self.sTeacher = sTeacher
    getPrereqs(self)
    smarter_scrapes(self)
    



class Requirement:
	def __init__(self, courses):
		self.courses = courses