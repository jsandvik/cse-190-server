from markr import db


class Class(db.Model):
    sec_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50))
    ucsd_id = db.Column(db.String(10), db.ForeignKey('faculty.ucsd_id'))

    
    def __init__(self, sec_id, course_name, ucsd_id):
        self.sec_id = sec_id
        self.course_name = course_name
        self.ucsd_id = ucsd_id

    def __repr__(self):
        return '<%r Class %r %r>' % (self.sec_id, self.course_name, self.ucsd_id)
        
class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    sec_id = db.Column(db.ForeignKey('class.sec_id'))
    
    def __init__(self, date, sec_id):
        self.date = date
        self.sec_id = sec_id
        
    def __repr__(self):
        return '<Lecture on %r>' % (self.date)

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
    answer_type = db.Column(db.String(50))
    lecture_id = db.Column(db.ForeignKey('lecture.id')) 
    time_limit = db.Column(db.Integer)
	
    def __init__(self, question, answer_type, lecture_id, time_limit):
        self.question = question
        self.answer_type = answer_type
        self.lecture_id = lecture_id 
        self.time_limit = time_limit
        
    def __repr__(self):
        return '<Lecture %r Question %r>' % (self.lecture_id, self.question)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    question = db.Column(db.Integer, db.ForeignKey('question.id'))
    is_correct = db.Column(db.Boolean)
    
    def __init__(self, text, question, is_correct):
        self.text = text
        self.question = question
        self.is_correct = is_correct
        
    def __repr__(self):
        return '<Answer %r>' % self.text
        
    @property
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'question': self.question,
            'is_correct': self.is_correct
        }