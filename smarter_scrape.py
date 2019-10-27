import requests
from bs4 import BeautifulSoup

class Course:
  def __init__(self, department, code):
    self.department = department
    self.code = code
    smarter_scrape(self)

def smarter_scrape(course):

  URL = "https://smartercapes.com/" + course.department + "/" + course.code
  
  r = requests.get(URL)

  soup = BeautifulSoup(r.content, 'html5lib')

  table = soup.findAll('li')

  teachers = []

  for row in table:
    teachers.append(row.text)

  course.teachers = teachers

  table = soup.findAll('h3')

  course.avg_time = table[-2].text

  course.avg_grade = table[-1].text
    
tempCourse = Course("CSE", "11")

print (tempCourse.avg_grade)

