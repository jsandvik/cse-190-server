from markr import db
from markr.models import Class, Question, Answer, Lecture

from markr.mod_auth.models import Faculty, Student

import datetime

db.drop_all()
db.create_all()

teacher = Faculty('628191', 'Ganz', '', 'Chockalingham')
db.session.add(teacher)
db.session.commit()

course = Class(123, "Mobile Programming", teacher.ucsd_id)
db.session.add(course)
db.session.commit()

lecture_1 = Lecture(datetime.datetime.utcnow(), course.sec_id)
db.session.add(lecture_1)
db.session.commit()

lecture_2 = Lecture(datetime.datetime.utcnow(), course.sec_id)
db.session.add(lecture_2)
db.session.commit() 

# First question
question = Question("Do you want to skip the final this quarter and instead, I just give everyone an A", "single_select", lecture_1.id)
db.session.add(question)
db.session.commit()

# First question's answers
answer_choice_1 = Answer("Yes", question.id, False)
answer_choice_2 = Answer("No", question.id, False)
answer_choice_3 = Answer("Just give me my A now", question.id, False)
answer_choice_4 = Answer("Make me work for my A", question.id, False)
db.session.add(answer_choice_1)
db.session.add(answer_choice_2)
db.session.add(answer_choice_3)
db.session.add(answer_choice_4)
db.session.commit()

# Second question
question2 = Question("What do you like about this class", "multi_select", lecture_1.id)
db.session.add(question2)
db.session.commit()

# Second question's answers
answer_choice_A = Answer("iOS", question2.id, False)
answer_choice_B = Answer("Backend", question2.id, False)
answer_choice_C = Answer("Frontend", question2.id, False)
answer_choice_D = Answer("Nothing", question2.id, False)
answer_choice_E = Answer("All of the above", question2.id, False)
db.session.add(answer_choice_A)
db.session.add(answer_choice_B)
db.session.add(answer_choice_C)
db.session.add(answer_choice_D)
db.session.add(answer_choice_E)
db.session.commit()

# Students
student_1 = Student("1234567890", "Larry", "", "Page")
student_2 = Student("0987654321", "Tim", "", "Cook")
db.session.add(student_1)
db.session.add(student_2)
db.session.commit()


print "DATABASE SEEDED!"
# teachers = Faculty.query.all()
# print teachers 
# 
# students = Student.query.all()
# print students
# 
# courses = Class.query.all()
# print courses
# 
# lectures = Lecture.query.all()
# print lectures
# 
# questions = Question.query.all()
# print questions
# 
# answers = Answer.query.all()
# print answers

