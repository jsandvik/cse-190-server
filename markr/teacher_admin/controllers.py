from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response
                  
from markr import db


teacher_admin = Blueprint('teacher_admin', __name__, 
                            url_prefix='/admin', template_folder='templates')

@teacher_admin.route('/', methods=['GET'])
def index():
    return render_template("questions.html")
