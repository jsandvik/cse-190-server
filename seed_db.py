from markr import db
from markr.models import Class, Question, Answer, Lecture

from markr.mod_auth.models import Faculty, Student
from markr.mod_vote.models import Vote

import datetime

db.drop_all()
db.create_all()

teacher = Faculty('628191', 'Ganz', '', 'Chockalingham')
db.session.add(teacher)
db.session.commit()

course = Class(123, "Mobile Programming", "Spring", 2014, "Tu/Th", datetime.time(12, 30), datetime.time(13, 50), teacher.ucsd_id)
db.session.add(course)
db.session.commit()

lecture_1 = Lecture(datetime.datetime.utcnow(), course.sec_id)
db.session.add(lecture_1)
db.session.commit()

lecture_2 = Lecture(datetime.datetime.utcnow(), course.sec_id)
db.session.add(lecture_2)
db.session.commit() 

# First question
question_str = "Do you want to skip the final this quarter and instead, I just give everyone an A"
question = Question(question_str, "single_select", lecture_1.id, True)
db.session.add(question)
db.session.commit()

# First question's answers
answer_choice_1 = Answer("Yes", question.id, True)
answer_choice_2 = Answer("No", question.id, False)
answer_choice_3 = Answer("Just give me my A now", question.id, False)
answer_choice_4 = Answer("Make me work for my A", question.id, False)
db.session.add(answer_choice_1)
db.session.add(answer_choice_2)
db.session.add(answer_choice_3)
db.session.add(answer_choice_4)
db.session.commit()

# Second question
question_str = "What do you like about this class"
question2 = Question(question_str, "multi_select", lecture_1.id, False)
db.session.add(question2)
db.session.commit()

# Second question's answers
answer_choice_A = Answer("iOS", question2.id, False)
answer_choice_B = Answer("Backend", question2.id, True)
answer_choice_C = Answer("Frontend", question2.id, True)
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

# Votes
vote = Vote(1, "1234567890", 1)
db.session.add(vote)
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

