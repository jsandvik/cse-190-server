from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

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

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
