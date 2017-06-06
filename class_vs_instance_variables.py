class BestCourse: #Define class BestCourse
	website = "http://cleverprogrammer.com" #Class wide variable

	def __init__(self, name):
		self.name = name

python_course = BestCourse("Learn Python")
learn_command_line_course = BestCourse("Learn Command Line")

print(python_course.name) #OBJECT_NAME.METHOD
print(BestCourse.website) #CLASS_NAME.METHOD

print(learn_command_line_course.name)
print(BestCourse.website)