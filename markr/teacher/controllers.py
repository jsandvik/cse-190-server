from flask import Blueprint, jsonify
from markr import db
from markr.models import Class

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
