from bs4 import BeautifulSoup

import requests
import unicodedata

# Get the html data in raw format
r = requests.get("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesPreReq.htm?termCode=FA19&courseId=CSE101");
data = r.text
soup = BeautifulSoup(data, features="html.parser")

# Create an array of elements from the table data, deleting the first row
table = soup.findAll('span')
elements = []
for i in table:
	elements.append(i.get_text().strip())
del elements[0]

# If there is only one prereq, add it and return
prereqs = []
if(len(elements) == 1):
	prereqs.append([])
	prereqs[0].append(elements[0])
	print(prereqs)
	exit()

# Populate the prereqs data array
# List of lists of classes that fulfil the same prereq
i = 0
j = -1
while(i < len(elements) - 1):
	
	# Use the "or" in the table to differentiate between classes fulfilling the same prereq
	prereqs.append([])
	j += 1
	prereqs[j].append(elements[i])
	i += 1
	while(i < len(elements) - 1 and elements[i].find("or") > -1):
		prereqs[j].append(elements[i + 1])
		i += 2

print(prereqs)
