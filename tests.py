"""
    Unit tests for markr
"""

from markr import app, db
from markr.mod_auth.models import Student
import unittest

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/testDB'
        self.app = app.test_client()
        db.create_all()

    def test_voting(self):
        """
            Tests the URL that adds a vote to the database
        """

        student = Student(123, 'test', 'test', 'test')
        db.session.add(student)
        db.session.commit()

        # Valid vote
        response = self.app.post('/vote/', data=dict(vote='a', pid=123))
        assert response.status == "200 OK"

        # Invalid votes
        response = self.app.post('/vote/', data=dict(pid=123))
        assert response.status == "400 BAD REQUEST"

        response = self.app.post('/vote/', data=dict(vote='b'))
        assert response.status == "400 BAD REQUEST"

        response = self.app.post('/vote/')
        assert response.status == "400 BAD REQUEST"

    def test_add_student(self):
        """
            Tests the URL that adds a student to the database.
        """

        # Valid student addition
        post_data = {
            "pid" : "A08868171",
            "f_name" : "John",
            "m_name" : "W",
            "l_name" : "Smith",
        }
        response = self.app.post('/auth/add-student/', data=post_data)
        assert response.status == "200 OK"

        # Valid student addition (middle name optional)
        post_data = {
            "pid" : "A09999999",
            "f_name" : "Jimmy",
            "l_name" : "Bananas",
        }
        response = self.app.post('/auth/add-student/', data=post_data)
        assert response.status == "200 OK"

        # Invalid student addition (pid exists already)
        post_data = {
            "pid" : "A09999999",
            "f_name" : "Jimmy",
            "l_name" : "Bananas",
        }
        response = self.app.post('/auth/add-student/', data=post_data)
        assert response.status == "400 BAD REQUEST"

        # Invalid student addition (last name missing)
        post_data = {
            "pid" : "A01234567",
            "f_name" : "Jimmy",
        }
        response = self.app.post('/auth/add-student/', data=post_data)
        assert response.status == "400 BAD REQUEST"

        # Invalid student addition (first name missing)
        post_data = {
            "pid" : "A04444444",
            "l_name" : "Bananas",
        }
        response = self.app.post('/auth/add-student/', data=post_data)
        assert response.status == "400 BAD REQUEST"

        # Invalid student addition (pid missing)
        post_data = {
            "f_name" : "Jimmy",
            "l_name" : "Bananas",
        }
        response = self.app.post('/auth/add-student/', data=post_data)
        assert response.status == "400 BAD REQUEST"

        # Invalid student addition (missing all data)
        response = self.app.post('/auth/add-student/', data={})
        assert response.status == "400 BAD REQUEST"

    def test_add_faculty(self):
        """
            Tests the URL that adds a teacher to the database.
        """

        # Valid faculty addition
        post_data = {
            "ucsd_id" : "jsmith@ucsd.edu",
            "f_name" : "John",
            "m_name" : "W",
            "l_name" : "Smith",
        }
        response = self.app.post('/auth/add-faculty/', data=post_data)
        assert response.status == "200 OK"

        # Valid faculty addition (middle name optional)
        post_data = {
            "ucsd_id" : "jbananas@ucsd.edu",
            "f_name" : "Jimmy",
            "l_name" : "Bananas",
        }
        response = self.app.post('/auth/add-faculty/', data=post_data)
        assert response.status == "200 OK"

        # Invalid faculty addition (ucsd email exists already)
        post_data = {
            "ucsd_id" : "jbananas@ucsd.edu",
            "f_name" : "Jimmy",
            "l_name" : "Bananas",
        }
        response = self.app.post('/auth/add-faculty/', data=post_data)
        assert response.status == "400 BAD REQUEST"

        # Invalid faculty addition (last name missing)
        post_data = {
            "ucsd_id" : "jimmy@ucsd.edu",
            "f_name" : "Jimmy",
        }
        response = self.app.post('/auth/add-faculty/', data=post_data)
        assert response.status == "400 BAD REQUEST"

        # Invalid faculty addition (first name missing)
        post_data = {
            "ucsd_id" : "bananas@ucsd.edu",
            "l_name" : "Bananas",
        }
        response = self.app.post('/auth/add-faculty/', data=post_data)
        assert response.status == "400 BAD REQUEST"

        # Invalid faculty addition (ucsd email missing)
        post_data = {
            "f_name" : "Jimmy",
            "l_name" : "Bananas",
        }
        response = self.app.post('/auth/add-faculty/', data=post_data)
        assert response.status == "400 BAD REQUEST"

        # Invalid faculty addition (missing all data)
        response = self.app.post('/auth/add-faculty/', data={})
        assert response.status == "400 BAD REQUEST"

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
