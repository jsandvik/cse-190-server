from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response, Response
                  
import csv
from markr import db
from markr.models import Question, Answer, Lecture, Class
from datetime import datetime, timedelta

teacher_admin = Blueprint('teacher_admin', __name__, url_prefix='/admin')

@teacher_admin.route('/classes/<int:faculty_id>/', methods=['GET', 'POST'])
def classes(faculty_id):
    """
        View function for adding and removing classes for a teacher
    """
    if request.method == "POST":
        class_name = request.form.get("class-name", "", str)
        quarter = request.form.get("quarter", "", str)
        days_of_week = request.form.get("schedule", "", str)
        start_time_str = request.form.get("start-time", "", str)
        end_time_str = request.form.get("end-time", "", str)
        year = request.form.get("year", 0, int)
        section_id = request.form.get("section-id", 0, int)

        if not class_name:
            class_name = request.form.get("new-class-name", "", str)

        if class_name and quarter and year and section_id and days_of_week and start_time_str and end_time_str:
            start_time = datetime.strptime(start_time_str, '%I:%M %p').time()
            end_time = datetime.strptime(end_time_str, '%I:%M %p').time()

            section = Class(section_id, class_name, quarter, year, days_of_week, start_time, end_time, faculty_id)
            db.session.add(section)
            db.session.commit()

            state_date_str = request.form.get("start-date", "", str)
            end_date_str = request.form.get("end-date", "", str)
            start_date = datetime.strptime(state_date_str, "%m/%d/%Y")        
            end_date = datetime.strptime(end_date_str, "%m/%d/%Y")
            step = timedelta(days=1)

            dates = []
            while start_date <= end_date:
                weekday = start_date.weekday()
                if days_of_week == "M/W/F" and (weekday == 0 or weekday == 2 or weekday == 4):
                    dates.append(start_date)
                elif days_of_week == "Tu/Th" and (weekday == 1 or weekday == 3):
                    dates.append(start_date)
                elif days_of_week == "M/W" and (weekday == 0 or weekday == 2):
                    dates.append(start_date)
                start_date += step

            for date in dates:
                lecture = Lecture(date, section_id)
                db.session.add(lecture)
            db.session.commit()

    classes = db.session.query(Class).filter(Class.ucsd_id == faculty_id).order_by(Class.year.asc(), Class.quarter.asc()).all()

    unique_class_names = [x[0] for x in db.session.query(Class.course_name).distinct()]
    return render_template("teacher_admin/classes.html",
                            classes=classes,
                            unique_class_names=unique_class_names)

@teacher_admin.route('/lectures/<int:section_id>/', methods=['GET', 'POST'])
def lectures(section_id):
    """
        View function for editing and viewing lectures in a section
    """
    if request.method == "POST":
        lecture_id = request.form.get("delete-lecture", None, int)
        add_lecture = request.form.get("add-lecture", None, int)
        export_csv = request.form.get("export-csv", None, int)
        if lecture_id != None:
            lecture = db.session.query(Lecture).filter(Lecture.id == lecture_id).one()
            db.session.delete(lecture)
            db.session.commit()

        if add_lecture != None:
            date_str = request.form.get("date", "", str)
            date = datetime.strptime(date_str, "%m/%d/%Y")
            lecture = Lecture(date, section_id)
            db.session.add(lecture)
            db.session.commit()

        if export_csv != None:
            return export_attendance()

    lectures = db.session.query(Lecture).filter(Lecture.sec_id == section_id).order_by(Lecture.date.asc()).all()

    for lecture in lectures:
        questions = db.session.query(Question).filter(Question.lecture_id == lecture.id).all()
        lecture.count = len(questions)

    # Get the section the lectures belong to
    section = db.session.query(Class).filter(Class.sec_id == section_id).one()

    return render_template("teacher_admin/lectures.html",
                            lectures=lectures,
                            section=section)

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
            question = Question(question_body, "single_select", lecture_id, True)
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
    entry["question"] = questions.append(Question("", "single_select", 1, True))
    entry["answers"] = zip([Answer("", "", 0), Answer("", "", 0)], letters)
    entries.append(entry)

    # Get the lecture
    lecture = db.session.query(Lecture).filter(Lecture.id == lecture_id).one()

    # Also get the section
    section = db.session.query(Class).filter(Class.sec_id == lecture.sec_id).one()

    # Get the previous and next lectures for navigation
    all_lectures = db.session.query(Lecture).filter(Lecture.sec_id == lecture.sec_id).order_by(Lecture.date.asc()).all()

    for i, entry in enumerate(all_lectures):
        if entry.id == lecture.id:
            if i - 1 >= 0:
                previous_lecture = all_lectures[i - 1]
            else:
                previous_lecture = None
            if i + 1 < len(all_lectures):
                next_lecture = all_lectures[i + 1]
            else:
                next_lecture = None

    return render_template("teacher_admin/questions.html", 
                            entries=entries,
                            lecture=lecture,
                            previous_lecture=previous_lecture,
                            next_lecture=next_lecture,
                            section=section)

def export_attendance():
    """
        Exports a csv file with a list of all students that have voted for the 
        corresponding questions in all the lectures of a given class.
    """
    pass
