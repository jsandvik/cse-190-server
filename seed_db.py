from markr import db, Class, Question, Answer

from markr.mod_auth.models import Faculty, Student

db.drop_all()
db.create_all()

teacher = Faculty('628191', 'Ganz', '', 'Chockalingham')
db.session.add(teacher)
db.session.commit()

course = Class(123, "Mobile Programming", teacher.ucsd_id)
db.session.add(course)
db.session.commit()

question = Question("Do you want to skip the final this quarter and instead, I just give everyone an A", course.sec_id, "single-select")
db.session.add(question)
db.session.commit()

answer_choice_1 = Answer("Yes", question.id, False)
answer_choice_2 = Answer("No", question.id, False)
answer_choice_3 = Answer("Just give me my A now", question.id, False)
answer_choice_4 = Answer("Make me work for my A", question.id, False)
db.session.add(answer_choice_1)
db.session.add(answer_choice_2)
db.session.add(answer_choice_3)
db.session.add(answer_choice_4)
db.session.commit()

student_1 = Student("1234567890", "Larry", "", "Page")
student_2 = Student("0987654321", "Tim", "", "Cook")
db.session.add(student_1)
db.session.add(student_2)
db.session.commit()


teachers = Faculty.query.all()
print teachers 

students = Student.query.all()
print students

courses = Class.query.all()
print courses

questions = Question.query.all()
print questions

answers = Answer.query.all()
print answers

