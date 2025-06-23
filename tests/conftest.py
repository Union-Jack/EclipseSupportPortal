# Tests were written follwing the 'Testing Flask Applications' Flask documentation (Flask, no date).
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))
from app_factory import create_app
from extensions import db
from models.ticket_model import TicketModel
from models.user_model import UserModel
from models.comment_model import CommentModel

#Setup the test client
@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' 
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all() 
        yield testing_client  
        with app.app_context():
            db.drop_all() 

#Crete a new test standard user
@pytest.fixture
def test_user(test_client):
    response = test_client.post('/register', data={
        'username': 'TestUser',
        'password': 'SecurePass1!'
    }, follow_redirects=True)

    assert response.status_code == 200

    with db.session() as session:
        user = session.query(UserModel).filter_by(username="TestUser").first()
    
    assert user is not None 
    return {"username": "TestUser", "password": "SecurePass1!", "user_id": user.id}

#Create a test admin user
@pytest.fixture
def test_admin(test_client):
    response = test_client.post('/register', data={
        'username': 'AdminUser',
        'password': 'SecurePass1!',
        'admin': 1
    }, follow_redirects=True)

    assert response.status_code == 200

    with db.session() as session:
        admin = session.query(UserModel).filter_by(username="AdminUser").first()
    
    assert admin is not None 
    return {"username": "AdminUser", "password": "SecurePass1!", "user_id": admin.id}

#Login helper function
def login(test_client, username, password):
    return test_client.post('/login', data={
        'username': username,
        'password': password
    }, follow_redirects=True) 

#Seed a test ticket created by an admin
@pytest.fixture
def admin_ticket(test_admin):
    with db.session() as session:
        ticket = TicketModel(title="Sample Admin Ticket", description="This is a test ticket created by an admin.", author_id=test_admin["user_id"])        
        session.add(ticket)  
        session.commit()  
        return {"ticket_id": ticket.id}

#Seed a test ticket created by a user
@pytest.fixture
def user_ticket(test_user):
    with db.session() as session:
        ticket = TicketModel(title="Sample User Ticket", description="This is a test ticket created by a user.", author_id=test_user["user_id"])        
        session.add(ticket)  
        session.commit()  
        return {"ticket_id": ticket.id}

#Seed a test ticket created by an admin
@pytest.fixture
def admin_comment(test_admin, admin_ticket):
    with db.session() as session:
        comment = CommentModel(
            content="This is an admin test comment.",
            author_id=test_admin["user_id"],
            ticket_id=admin_ticket["ticket_id"]
        )
        session.add(comment)
        session.commit()

        return {"comment_id": comment.id}

#Seed a comment created by a user
@pytest.fixture
def user_comment(test_user, user_ticket):
    with db.session() as session:
        comment = CommentModel(
            content="This is a user test comment.",
            author_id=test_user["user_id"],
            ticket_id=user_ticket["ticket_id"]
        )
        session.add(comment)
        session.commit()

        return {"comment_id": comment.id}
