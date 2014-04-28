from markr import db

class User(db.Model):
    __abstract__ = True
    l_name = db.Column(db.String(20), nullable = False)
    f_name = db.Column(db.String(20), nullable = False)
    m_name = db.Column(db.String(20), nullable = True)
    
    
class Student(User):
    pid = db.Column(db.String(10), primary_key = True)
    
    def __init__(self, pid, f_name, m_name, l_name):
        self.pid = pid
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name

    def __repr__(self):
        return '<Student %r>' % (self.f_name + self.l_name)
        
class Faculty(User):
    username = db.Column(db.String(20), primary_key = True)
    
    def __init__(self, username, f_name, m_name, l_name):
        self.username = username
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        
    def __repr__(self):
        return '<Faculty %r' % (self.f_name + self.l_name)