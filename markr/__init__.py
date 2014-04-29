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
from markr.teacher_admin.controllers import teacher_admin as teacher_module

# Register blueprints
app.register_blueprint(auth_module)
app.register_blueprint(vote_module)
app.register_blueprint(teacher_module)

class Class(db.Model):
    sec_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50))
    ucsd_id = db.Column(db.String(10), db.ForeignKey('faculty.ucsd_id'))
    
    def __init__(self, sec_id, course_name, ucsd_id):
        self.sec_id = sec_id
        self.course_name = course_name
        self.ucsd_id = ucsd_id

    def __repr__(self):
        return '<%r Class %r>' % (self.sec_id, self.course_name)

class Access(db.Model):
    id = db.Column(db.Integer, primary_key=True) # need to specify primary key for table
    class_date = db.Column(db.DateTime)
    token = db.Column(db.String(10))
    sec_id = db.Column(db.Integer, db.ForeignKey('class.sec_id'))
	
    def __init__(self, class_date, token):
        self.class_date = class_date
        self.token = token

    def __repr__(self):
        return '<Access %r>' % (self.class_date + self.token)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True) # need to specify primary key for table
    question = db.Column(db.Text)
    sec_id = db.Column(db.Integer, db.ForeignKey('class.sec_id')) 
    
    def __init__(self, question, sec_id):
        self.question = question
        self.sec_id = sec_id
        
    def __repr__(self):
        return '<Question %r>' % (self.question)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    question = db.Column(db.Integer, db.ForeignKey('question.id'))
    is_correct = db.Column(db.Boolean)
    type = db.Column(db.String(20))
    
    def __init__(self, text, question, is_correct):
        self.text = text
        self.question = question
        self.is_correct = is_correct
        
    def __repr__(self):
        return '<Answer %r>' % self.text
    


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
