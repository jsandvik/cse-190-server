from markr import app, db, Student
import unittest
import tempfile

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/testDB'
        self.app = app.test_client()
        db.create_all()

    def test_voting(self):
        student = Student(123, 'test', 'test', 'test')
        db.session.add(student)
        db.session.commit()

        # Valid vote
        response = self.app.post('/vote/', data=dict(vote='a',pid=123))
        assert response.status == "200 OK"

        # Invalid votes
        response = self.app.post('/vote/', data=dict(pid=123))
        assert response.status == "400 BAD REQUEST"

        response = self.app.post('/vote/', data=dict(vote='b'))
        assert response.status == "400 BAD REQUEST"

        response = self.app.post('/vote/')
        assert response.status == "400 BAD REQUEST"

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
