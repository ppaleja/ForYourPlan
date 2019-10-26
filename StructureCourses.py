class DegreeRequirment:
	def __init__(self, courses):
		self.courses = courses

class Course:
	def __init__(self, department, code):
		self.department = department
		self.code = code


f = open("cse-major-course-reqs.txt", "r")

lines = f.read().split("\n")
#print(lines)

degreeReqs = []
for idx, line in enumerate(lines):
	line.strip()
	courses = line.split(",")
	degreeReqs.append([])
	for course in courses:
		course.strip()
		courseArray = course.split(" ")
		courseElement = Course(courseArray[0], courseArray[1])
		degreeReqs[idx].courses.append

# Make list of degree requirements


