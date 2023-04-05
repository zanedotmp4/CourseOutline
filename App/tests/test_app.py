import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
    get_user,
    get_user_by_username,
    update_user
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bobpass","bob@mail.com")
        assert user.email == "bob@mail.com"

    # pure function no side effects or integrations called
    def test_toJSON(self):
        user = User("bobpass","bob@mail.com")
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {"id":None,"email":"bob@mail.com"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password,"bob@mail.com")
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password,"bob@mail.com")
        assert user.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    user = create_user("bobpass","bob@mail.com","Lecture",True)
    assert authenticate("bobpass","bob@mail.com","Lecture",True) != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("bobpass","rick@mail.com","Lecture",True)
        assert user.email == "rick@mail.com"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1,"email":"bob@mail.com"}, {"id":2,"email":"rick@mail.com"}], users_json)

