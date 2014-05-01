from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response
                  
from markr import db
from markr.models import Question, Answer

teacher_admin = Blueprint('teacher_admin', __name__, url_prefix='/admin')

@teacher_admin.route('/', methods=['GET', 'POST'])
def index():
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
            question = Question(question_body, "single_select", 1)
            db.session.add(question)
            db.session.commit()
            
            for i, answer_text in enumerate(answers_text):
                answer = Answer(answer_text, question.id, i == correct_answer)
                db.session.add(answer)

            db.session.commit()
        elif action == "edit":
            pass
        elif action == "delete":
            answers = db.session.query(Answer).filter(Answer.question == question_id).all()
            for answer in answers:
                db.session.delete(answer)
            db.session.commit()
            
            question = db.session.query(Question).filter(Question.id == question_id).one()
            db.session.delete(question)
            db.session.commit()

    entries = []
    questions = db.session.query(Question).filter(Question.lecture_id == 1).all()   
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
    entry["question"] = questions.append(Question("", "single_select", 1))
    entry["answers"] = zip([Answer("", "", 0), Answer("", "", 0)], letters)
    entries.append(entry)

    return render_template("teacher_admin/questions.html", 
                            entries=entries)
