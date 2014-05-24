from flask import Blueprint, jsonify
from markr.mod_vote.models import Vote
from markr.models import Question, Lecture, Class, Answer

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

    unique_sections = []
    section_ids = []
    for section in sections:
        if section.sec_id not in section_ids:
            section_ids.append(section.sec_id)
            unique_sections.append(section)

    sections = [x.serialize for x in unique_sections]
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

    unique_lectures = []
    lecture_ids = []
    for lecture in lectures:
        if lecture.id not in lecture_ids:
            lecture_ids.append(lecture.id)
            unique_lectures.append(lecture)

    lectures = [x.serialize for x in unique_lectures]
    data = {
        "data" : lectures
    }

    return jsonify(data)

@student.route('/questions/<student_id>/<lecture_id>/', methods=["GET"])
def get_questions(student_id, lecture_id):
    votes = Vote.query.filter_by(pid=student_id)

    questions = []
    for vote in votes:
        questions.extend(Question.query.filter_by(id=vote.question_id, lecture_id=lecture_id))

    unique_questions = []
    question_ids = []
    for question in questions:
        if question.id not in question_ids:
            question_ids.append(question.id)
            unique_questions.append(question)

    questions = [x.serialize for x in unique_questions]
    data = {
        "data" : questions
    }

    return jsonify(data)

@student.route("/answers/<student_id>/<question_id>/", methods=['GET'])
def get_answers_with_vote(student_id, question_id):
    vote = Vote.query.filter_by(pid=student_id, question_id=question_id).one()

    vote = vote.serialize

    answers = Answer.query.filter_by(question=question_id)
    answers = [x.serialize for x in answers]

    data = {
        "vote" : vote,
        "answers" : answers
    }

    return jsonify(data)
