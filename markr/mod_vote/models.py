from markr import db

class Vote(db.Model):
    vote = db.Column(db.String(1))
    question_id = db.Column(db.String(10))
    pid = db.Column(db.String(10), db.ForeignKey('student.pid'))
    
    def __init__(self, vote, pid, question_id):
        self.vote = vote
        self.pid = pid
        self.question_id = question_id

    def __repr__(self):
        return '<%r voted %r>' % self.pid, self.vote