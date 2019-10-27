from PrereqScraper import getPrereqs

class Requirement:
	def __init__(self, courses):
		self.courses = courses

class Course:
	def __init__(self, department, code):
		self.department = department
		self.code = code
		self.prereqs = getPrereqs(department, code)
		

f = open("cse-major-course-reqs.txt", "r")

lines = f.read().split("\n")
#print(lines)

degreeReqs = []
for idx, line in enumerate(lines):
	line.strip()
	courses = line.split(",")
	degreeReqs.append(Requirement([]))
	for course in courses:
		course.strip()
		courseArray = course.split(" ")
		degreeReqs[idx].courses.append(Course(courseArray[0], courseArray[1]))

for x in degreeReqs:
	for y in x.courses:
		print(y.code)

# Make list of degree requirements


