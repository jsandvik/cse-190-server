from markr import db

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.Integer, db.ForeignKey('answer.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    pid = db.Column(db.String(10), db.ForeignKey('student.pid'))
    
    def __init__(self, vote, pid, question_id):
        self.vote = vote
        self.pid = pid
        self.question_id = question_id

    def __repr__(self):
        return '<%r voted %r>' % (self.pid, self.vote)