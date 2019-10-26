import requests
from bs4 import BeautifulSoup

url='https://cse.ucsd.edu/undergraduate/2018-2019-tentative-undergraduate-course-offerings'

data = requests.get(url).text
soup = BeautifulSoup(data, features="html.parser")

table = soup.findAll('td')
#elements = []

class Course:
	def __init__(self, code, name, fTeacher, wTeacher, sTeacher):
		self.code = code
		self.name = name
		self.fTeacher = fTeacher
		self.wTeacher = wTeacher
		self.sTeacher = sTeacher



courses = []
i = 7
while(i < len(table) - 4):
	courses.append(Course(table[i].get_text().strip(),
						  table[i + 1].get_text().strip(),
						  table[i + 2].get_text().strip(),
						  table[i + 3].get_text().strip(),
						  table[i + 4].get_text().strip()))
	i = i + 5 + 2
	
for x in courses:
	print(x.code)