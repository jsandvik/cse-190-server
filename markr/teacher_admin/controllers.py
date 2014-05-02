from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response
                  
from markr import db
from markr.models import Question, Answer, Lecture, Class
from datetime import datetime, timedelta

teacher_admin = Blueprint('teacher_admin', __name__, url_prefix='/admin')

@teacher_admin.route('/classes/<int:faculty_id>/', methods=['GET'])
def classes(faculty_id):
    """
        View function for adding and removing classes for a teacher
    """

    classes = db.session.query(Class).filter(Class.ucsd_id == faculty_id).all()
    return render_template("teacher_admin/classes.html",
                            classes=classes)

@teacher_admin.route('/lectures/<int:section_id>/', methods=['GET', 'POST'])
def lectures(section_id):
    """
        View function for editing and viewing lectures in a section
    """
    if request.method == "POST":
        lecture_id = request.form.get("delete-lecture", None, int)
        if lecture_id != None:
            lecture = db.session.query(Lecture).filter(Lecture.id == lecture_id).one()
            db.session.delete(lecture)
            db.session.commit()
        else:
            schedule = request.form.get("schedule", 0, int)
            state_date_str = request.form.get("start-date", "", str)
            end_date_str = request.form.get("end-date", "", str)
            start_date = datetime.strptime(state_date_str, "%m/%d/%Y")        
            end_date = datetime.strptime(end_date_str, "%m/%d/%Y")
            step = timedelta(days=1)

            dates = []
            while start_date <= end_date:
                weekday = start_date.weekday()
                if schedule == 1 and (weekday == 0 or weekday == 2 or weekday == 4):
                    dates.append(start_date)
                elif schedule == 2 and (weekday == 1 or weekday == 3):
                    dates.append(start_date)
                elif schedule == 3 and (weekday == 0 or weekday == 2):
                    dates.append(start_date)
                start_date += step

            for date in dates:
                lecture = Lecture(date, 123)
                db.session.add(lecture)
            db.session.commit()

    lectures = db.session.query(Lecture).filter(Lecture.sec_id == section_id).order_by(Lecture.date.asc()).all()
    return render_template("teacher_admin/lectures.html",
                            lectures=lectures)

@teacher_admin.route('/questions/<int:lecture_id>/', methods=['GET', 'POST'])
def questions(lecture_id):
    """
        View function for editing questions in a lecture
    """

    if request.method == "POST":
        # Get POST data
        question_body = request.form.get("question", "", str)
        answers_text = request.form.getlist("answers", str)
        correct_answer = request.form.get("correct-answer", None, int)
        action = request.form.get("action", None, str)
        question_id = request.form.get("question-id", None, int)

        if action == "add":
            question = Question(question_body, "single_select", lecture_id, 0, True)
            db.session.add(question)
            db.session.commit()
            
            for i, answer_text in enumerate(answers_text):
                answer = Answer(answer_text, question.id, i == correct_answer)
                db.session.add(answer)

            db.session.commit()
        elif action == "edit":
            # Update the question
            question = db.session.query(Question).filter(Question.id == question_id).one()
            question.question = question_body
            db.session.add(question)
            db.session.commit()

            # First delete all current answers
            answers = db.session.query(Answer).filter(Answer.question == question_id).all()
            for answer in answers:
                db.session.delete(answer)
            db.session.commit()

            # Then add new answers
            for i, answer_text in enumerate(answers_text):
                answer = Answer(answer_text, question.id, i == correct_answer)
                db.session.add(answer)
            db.session.commit()
        elif action == "delete":
            answers = db.session.query(Answer).filter(Answer.question == question_id).all()
            for answer in answers:
                db.session.delete(answer)
            db.session.commit()

            question = db.session.query(Question).filter(Question.id == question_id).one()
            db.session.delete(question)
            db.session.commit()

    entries = []
    questions = db.session.query(Question).filter(Question.lecture_id == lecture_id).all()   
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for question in questions:
        entry = {}
        answers = db.session.query(Answer).filter(Answer.question == question.id).all()
        entry["question"] = question
        entry["answers"] = zip(answers, letters)
        entries.append(entry)

    # Create a brand new question that can be added by the user
    entry = {}
    entry["question"] = questions.append(Question("", "single_select", 1, 0, True))
    entry["answers"] = zip([Answer("", "", 0), Answer("", "", 0)], letters)
    entries.append(entry)

    return render_template("teacher_admin/questions.html", 
                            entries=entries)
