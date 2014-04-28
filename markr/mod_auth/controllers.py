from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response
                  
from markr import db

from markr.mod_auth.models import Student, Faculty

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/add-student/', methods=['POST'])
def add_student():
    """
        Adds the student to the database.
    """
    pid = request.form.get("pid", None, str)
    first_name = request.form.get("f_name", None, str)
    middle_name = request.form.get("m_name", None, str)
    last_name = request.form.get("l_name", None, str)

    # Return error if required data is missing
    if not first_name or not last_name or not pid:
        return make_response("error", 400)

    # Return error if student already exists with this PID
    count = db.session.query(Student).filter(Student.pid == pid).count()
    if count > 0:
        return make_response("error", 400)

    # Insert new student
    student = Student(pid, first_name, middle_name, last_name)
    db.session.add(student)
    db.session.commit()

    return make_response("done", 200)

@mod_auth.route('/login/', methods=['GET', 'POST'])
def login():
    
    # login checks here
    
    return render_template("auth/login.html")