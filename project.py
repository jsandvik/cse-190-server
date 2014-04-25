from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, make_response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cse190ucsd@localhost/appDB'
db = SQLAlchemy(app)

class Student(db.Model):
    pid = db.Column(db.String(10), primary_key=True)
    l_name = db.Column(db.String(20))
    f_name = db.Column(db.String(20))
    m_name = db.Column(db.String(20), nullable = True)

    def __init__(self, pid, f_name, m_name, l_name):
        self.pid = pid
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name

    def __repr__(self):
        return '<Student %r>' % (self.f_name + self.l_name)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.String(1))
    question_id = db.Column(db.String(10))
    pid = db.Column(db.String(10), db.ForeignKey('student.pid'))
    
    def __init__(self, vote, pid, question_id):
        self.vote = vote
        self.pid = pid
        self.question_id = question_id

    def __repr__(self):
        return '<%r voted %r>' % self.pid, self.vote

@app.route('/')
def hello_world():
   vote = Vote("a", 123, 0) 
   db.session.add(vote)
   db.session.commit()
   return make_response(render_template('index.html'), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
