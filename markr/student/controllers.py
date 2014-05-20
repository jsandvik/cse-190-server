from flask import Blueprint, jsonify
from markr.mod_vote.models import Vote
from markr.models import Question, Lecture, Class

student = Blueprint('student', __name__, url_prefix='/student')

@student.route('/classes/<student_id>/', methods=["GET"])
def get_classes(student_id):
    """
        This returns a json response of all the classes that the 
        given student has voted in
    """
    votes = Vote.query.filter_by(pid=student_id)

    questions = []
    for vote in votes:
        questions.extend(Question.query.filter_by(id=vote.question_id))

    lectures = []
    for question in questions:
        lectures.extend(Lecture.query.filter_by(id=question.lecture_id))

    sections = []
    for lecture in lectures:
        sections.extend(Class.query.filter_by(sec_id=lecture.sec_id))

    sections = [x.serialize for x in sections]
    data = {
        "data" : sections
    }

    return jsonify(data)

@student.route('/lectures/<student_id>/<class_id>/', methods=["GET"])
def get_lectures(student_id, class_id):
    """
        This returns a json response of all the lectures of a given class 
        that a student has votes in.
    """

    votes = Vote.query.filter_by(pid=student_id)

    questions = []
    for vote in votes:
        questions.extend(Question.query.filter_by(id=vote.question_id))

    lectures = []
    for question in questions:
        lectures.extend(Lecture.query.filter_by(id=question.lecture_id, sec_id=class_id))

    lectures = [x.serialize for x in lectures]
    data = {
        "data" : lectures
    }

    return jsonify(data)
