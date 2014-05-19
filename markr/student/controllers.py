from flask import Blueprint, jsonify
from markr import db
from markr.models import Class, Lecture, Question, Answer

student = Blueprint('student', __name__, url_prefix='/student')

@student.route('/classes/<student_id>/', methods=["GET"])
def get_classes(student_id):
    """
        This returns a json response of all the classes that the 
        given student has voted in
    """

    data = {
        "data" : []
    }

    return jsonify(data)
