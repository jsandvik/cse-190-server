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
    answer_type = db.Column(db.String(50))
    
    def __init__(self, question, sec_id, answer_type):
        self.question = question
        self.sec_id = sec_id
        self.answer_type = answer_type
        
    def __repr__(self):
        return '<Question %r>' % (self.question)

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