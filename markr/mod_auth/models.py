from markr import db

class Student(db.Model):
    pid = db.Column(db.String(10), primary_key=True)
    l_name = db.Column(db.String(20))
    f_name = db.Column(db.String(20))
    m_name = db.Column(db.String(20), nullable=True)

    def __init__(self, pid, f_name, m_name, l_name):
        self.pid = pid
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name

    def __repr__(self):
        return '<Student %r>' % (self.f_name + self.l_name)
		
class Faculty(db.Model):
    ucsd_id = db.Column(db.String(10), primary_key=True)
    l_name_fac = db.Column(db.String(20))
    f_name_fac = db.Column(db.String(20))
    m_name_fac = db.Column(db.String(20), nullable=True)

    def __init__(self, ucsd_id, f_name_fac, m_name_fac, l_name_fac):
        self.ucsd_id = ucsd_id
        self.f_name_fac = f_name_fac
        self.m_name_fac = m_name_fac
        self.l_name_fac = l_name_fac

    def __repr__(self):
        return '<Faculty %r>' % (self.f_name_fac + ' ' + self.l_name_fac)
