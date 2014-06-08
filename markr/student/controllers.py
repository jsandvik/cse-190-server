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

    # This finds the proper lecture number for each lecture found
    all_lectures = Lecture.query.filter_by(sec_id=class_id).all()
    for lecture in lectures:
        for i, x in enumerate(all_lectures):
            if x.id == lecture["id"]:
                lecture["number"] = i + 1


    data = {
        "data" : lectures
    }

    return jsonify(data)

@student.route('/questions/<student_id>/<class_id>/', methods=["GET"])
def get_questions(student_id, class_id):

    # Get the votes
    votes = Vote.query.filter_by(pid=student_id).all()

    # Get the question and answers that go along with each vote
    questions_with_answers = []
    for vote in votes:
        question = Question.query.filter_by(id=vote.question_id).one()
        answers = Answer.query.filter_by(question=vote.question_id).all()
        student_answer = Answer.query.filter_by(id=vote.vote).one()
        questions_with_answers.append({
            "vote" : student_answer,
            "answers" : answers,
            "question" : question
        })

    # Get unique questions
    unique_questions_with_answers = []
    question_ids = []
    for entry in questions_with_answers:
        if entry["question"].id not in question_ids:
            question_ids.append(entry["question"].id)
            unique_questions_with_answers.append(entry)

    # Only display votes from the given lectures
    lectures = Lecture.query.filter_by(sec_id=class_id).all()
    filtered_questions_with_answers = []
    for entry in unique_questions_with_answers:
        for lecture in lectures:
            if entry["question"].lecture_id == lecture.id:
                filtered_questions_with_answers.append(entry)

    # Serialize the data
    for entry in filtered_questions_with_answers:
        entry["vote"] = entry["vote"].serialize
        entry["answers"] = [x.serialize for x in entry["answers"]]
        entry["question"] = entry["question"].serialize

    # Make sure lectures are grouped together
    result = sorted(filtered_questions_with_answers, key=lambda x: x["question"]["lecture_id"])

    data = {
        "data" : result
    }

    return jsonify(data)

