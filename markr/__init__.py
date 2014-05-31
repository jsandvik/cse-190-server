from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, make_response, request


# Configurations
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


# Import modules using blueprint handler variable
# (mod_auth)
from markr.mod_auth.controllers import mod_auth as auth_module
from markr.mod_vote.controllers import mod_vote as vote_module
from markr.teacher_admin.controllers import teacher_admin as teacher_admin_module
from markr.teacher.controllers import teacher as teacher_module
from markr.student.controllers import student as student_module

# Register blueprints
app.register_blueprint(auth_module)
app.register_blueprint(vote_module)
app.register_blueprint(teacher_admin_module)
app.register_blueprint(teacher_module)
app.register_blueprint(student_module)

import markr.controllers

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
