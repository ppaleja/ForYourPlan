from PrereqScraper import getPrereqs
from classes import Course

class Course:
	def __init__(self, department, code):
		self.department = department
		self.code = code
		#self.prereqs = PrereqScraper(department, code)

course = Course("CSE", "100")
print(getPrereqs(course))