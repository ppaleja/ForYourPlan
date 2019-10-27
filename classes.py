class Course:
  code = ""
  name = ""
  fTeacher = ""
  wTeacher = ""
  sTeacher = ""
  prereqs = []

  def __init__(self, department, code):
    self.department = department
    self.code = code
  
  """
  def __init__(self, department, code, name, fTeacher, wTeacher, sTeacher):
    self.department = department
    self.code = code
    self.name = name
    self.fTeacher = fTeacher
    self.wTeacher = wTeacher
    self.sTeacher = sTeacher
    getPrereqs(self)
    smarter_scrapes(self)
  """

class Requirement:
	def __init__(self, courses):
		self.courses = courses