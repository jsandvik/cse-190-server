from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response
                  
from markr import db
from markr.models import Question, Answer

teacher_admin = Blueprint('teacher_admin', __name__, url_prefix='/admin')

@teacher_admin.route('/', methods=['GET'])
def index():
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

    return render_template("teacher_admin/questions.html", 
                            entries=entries)
