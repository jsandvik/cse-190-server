from markr import db


class Class(db.Model):
    sec_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50))
    quarter = db.Column(db.Enum("Winter", "Spring", "Summer", "Fall", name="quarter"))
    year = db.Column(db.Integer)
    days_of_week = db.Column(db.Enum("M/W/F", "M/W", "Tu/Th", name="days_of_week"))
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    ucsd_id = db.Column(db.String(10), db.ForeignKey('faculty.ucsd_id'))
    
    def __init__(self, sec_id, course_name, quarter, year, days_of_week, start_time, end_time, ucsd_id):
        self.sec_id = sec_id
        self.course_name = course_name
        self.quarter = quarter
        self.year = year
        self.days_of_week = days_of_week
        self.start_time = start_time
        self.end_time = end_time
        self.ucsd_id = ucsd_id

    def __repr__(self):
        return '<%r Class %r %r>' % (self.sec_id, self.course_name, self.ucsd_id)

    @property
    def serialize(self):
        return {
            'sec_id': self.sec_id,
            'course_name': self.course_name,
            'quarter': self.quarter,
            'year': self.year,
            'days_of_week': self.days_of_week,
            'start_time': self.start_time.strftime("%I:%M %p"),
            'end_time': self.end_time.strftime("%I:%M %p"),
            'ucsd_id': self.ucsd_id
        }
        
class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    sec_id = db.Column(db.ForeignKey('class.sec_id'))
    
    def __init__(self, date, sec_id):
        self.date = date
        self.sec_id = sec_id
        
    def __repr__(self):
        return '<Lecture on %r>' % (self.date)

    @property
    def serialize(self):
        return {
            'date': str(self.date),
            'sec_id': self.sec_id,
            'id': self.id,
        }

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
    show_results = db.Column(db.Boolean)
	
    def __init__(self, question, answer_type, lecture_id, show_results):
        self.question = question
        self.answer_type = answer_type
        self.lecture_id = lecture_id 
        self.show_results = show_results
        
    def __repr__(self):
        return '<Lecture %r Question %r>' % (self.lecture_id, self.question)
        
    @property
    def serialize(self):
        return {
            'id': self.id,
            'text': self.question,
            'answer_type': self.answer_type,
            'lecture_id': self.lecture_id,
            'show_results': self.show_results
        }

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