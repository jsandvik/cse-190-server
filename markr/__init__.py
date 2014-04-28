from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, make_response, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cse190ucsd@localhost/appDB'
db = SQLAlchemy(app)

# Import modules using blueprint handler variable
# (mod_auth)
from markr.mod_auth.controllers import mod_auth as auth_module

# Register blueprints
app.register_blueprint(auth_module)

# class Student(db.Model):
#     pid = db.Column(db.String(10), primary_key=True)
#     l_name = db.Column(db.String(20))
#     f_name = db.Column(db.String(20))
#     m_name = db.Column(db.String(20), nullable = True)
# 
#     def __init__(self, pid, f_name, m_name, l_name):
#         self.pid = pid
#         self.f_name = f_name
#         self.m_name = m_name
#         self.l_name = l_name
# 
#     def __repr__(self):
#         return '<Student %r>' % (self.f_name + self.l_name)

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

@app.route('/vote/', methods=['POST'])
def vote():
    # Get POST args
    student_vote = request.form.get('vote', None, str)
    pid = request.form.get('pid', None, int)

    # deny requests that don't send arguments
    if not student_vote or not pid:
        return make_response('error', 400)

    # Insert new vote
    vote = Vote(student_vote, pid, 0) 
    db.session.add(vote)
    db.session.commit()

    return make_response('done', 200)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
