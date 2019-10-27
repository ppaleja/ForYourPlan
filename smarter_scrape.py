import requests
from bs4 import BeautifulSoup


def smarter_scrape(courseNums):

  URL = "https://smartercapes.com/CSE/"
  
  courses = []
  
  for num in courseNums:

    r = requests.get(URL + num)

    soup = BeautifulSoup(r.content, 'html5lib')
    
    course = {}
    
    course['name'] = 'CSE ' + num

    table = soup.findAll('li')
    
    teachers = []

    for row in table:
      teachers.append(row.text)

    course['teachers'] = teachers

    table = soup.findAll('h3')

    course['avg_time'] = table[-2].text

    course['avg_grade'] = table[-1].text

    courses.append(course)
    
  return courses
    
courseNums = ['3', '11']

print(smarter_scrape(courseNums))
