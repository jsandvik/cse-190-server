from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response
                  
from markr import db
from markr.models import Question, Answer

teacher_admin = Blueprint('teacher_admin', __name__, url_prefix='/admin')

@teacher_admin.route('/', methods=['GET'])
def index():
    question = db.session.query(Question).filter(Question.id == 1).one()
    answers = db.session.query(Answer).filter(Answer.question == 1).all()

    return render_template("teacher_admin/questions.html", question=question, answers=answers)
