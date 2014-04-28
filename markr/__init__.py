from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, make_response, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cse190ucsd@localhost/appDB'
db = SQLAlchemy(app)

# Import modules using blueprint handler variable
# (mod_auth)
from markr.mod_auth.controllers import mod_auth as auth_module
from markr.mod_vote.controllers import mod_vote as vote_module

# Register blueprints
app.register_blueprint(auth_module)
app.register_blueprint(vote_module)

class Class(db.Model):
    sec_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(10))
    ucsd_id = db.Column(db.String(10), db.ForeignKey('faculty.ucsd_id'))
    
    def __init__(self, sec_id, course_name, ucsd_id):
        self.sec_id = sec_id
        self.course_name = course_name
        self.ucsd_id = ucsd_id

    def __repr__(self):
        return '<%r Class %r>' % self.sec_id, self.course_name

class Access(db.Model):
    class_date = db.Column(db.DateTime)
    token = db.Column(db.String(10))
    sec_id = db.Column(db.Integer, db.ForeignKey('class.sec_id'))
	
    def __init__(self, vote, pid):
        self.class_date = class_date
        self.token = token

    def __repr__(self):
        return '<Accesss %r>' % (self.class_date + self.token)

class Questions(db.Model):
    question = db.Column(db.String(50))
    answer = db.Column(db.String(50))
	sec_id = db.Column(db.Integer, db.ForeignKey('class.sec_id')) 
    
    def __init__(self, vote, pid):
        self.class_date = class_date
        self.token = token
		self.sec_id = sec_id
    def __repr__(self):
        return '<Questions&Ansers %r %r>' % self.question,  % self.answer		


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
