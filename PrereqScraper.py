from bs4 import BeautifulSoup
from classes import Requirement, Course

import requests
import unicodedata

def getPrereqs(course):
	# Get the html data in raw format
	r = requests.get("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesPreReq.htm?termCode=FA19&courseId=" + 
				  str(course.department) + str(course.code))
	data = r.text
	soup = BeautifulSoup(data, features="html.parser")

	# Create an array of elements from the table data, deleting the first row
	table = soup.findAll('span')
	elements = []
	for i in table:
		elements.append(i.get_text().strip())

	if(len(elements) == 0):
		return []
	del elements[0]

	# If there is only one prereq, add it and return
	rawReqs = []
	if(len(elements) == 1):
		rawReqs.append([])
		rawReqs[0].append(elements[0])
		return cleanRawReqs(rawReqs)

	# Populate the prereqs data array
	# List of lists of classes that fulfil the same prereq
	i = 0
	j = -1
	while(i < len(elements) - 1):
		
		# Use the "or" in the table to differentiate between classes fulfilling the same prereq
		rawReqs.append([])
		j += 1
		rawReqs[j].append(elements[i])
		i += 1
		while(i < len(elements) - 1 and elements[i].find("or") > -1):
			rawReqs[j].append(elements[i + 1])
			i += 2
	#print(rawReqs)
	return cleanRawReqs(rawReqs)

# Takes a list of requirements of class strings, and turns them into a list of requirements with course instances
def cleanRawReqs(rawReqs):
	print(str(rawReqs))
	requirements = []
	for reqs in rawReqs:
		requirement = Requirement([])
		for rawCourse in reqs:
			splitClassArray = splitClass(rawCourse)
			course = Course(splitClassArray[0], splitClassArray[1])
			requirement.courses.append(course)
		requirements.append(requirement)
	return requirements



def splitClass(classString):
	# Takes in a class string (e.g "CSE21") and outputs an array ["Department", "Code"]
	for i, c in enumerate(classString):
		if c.isdigit():
			#print([classString[:i], classString[i:]])
			return [classString[:i], classString[i:]]


	print(prereqs)
