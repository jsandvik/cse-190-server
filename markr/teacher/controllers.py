from flask import Blueprint, jsonify
from markr import db
from markr.models import Class, Lecture, Question, Answer

teacher = Blueprint('teacher', __name__, url_prefix='/teacher')

@teacher.route('/classes/<faculty_id>/', methods=["GET"])
def get_classes(faculty_id):
    """
        This returns a json response of all the classes for the given
        faculty member (specified by the faculty_id)
    """
    classes = db.session.query(Class).filter(Class.ucsd_id == faculty_id).all()
    classes = [x.serialize for x in classes]

    data = {
        "data" : classes
    }

    return jsonify(data)

@teacher.route('/lectures/<int:section_id>/', methods=["GET"])
def get_lectures(section_id):
    """
        This returns a json response of all the lectures for a given section.
    """
    lectures = db.session.query(Lecture).filter(Lecture.sec_id == section_id).all()
    lectures = [x.serialize for x in lectures]

    data = {
        "data" : lectures
    }
    return jsonify(data)

@teacher.route('/questions/<int:lecture_id>/', methods=['GET'])
def get_questions(lecture_id):
    """
        This returns a json response of all the questions for a given lecture.
    """
    questions = db.session.query(Question).filter(Question.lecture_id == lecture_id).all()
    questions = [x.serialize for x in questions]

    for question in questions:
        answers = Answer.query.filter_by(question=question["id"]).all()
        question["number_of_options"] = len(answers)
        question["answers"] = [a.serialize for a in answers]

    data = {
        "data" : questions
    }
    return jsonify(data)
