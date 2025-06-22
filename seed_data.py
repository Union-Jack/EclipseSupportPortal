from extensions import db, bcrypt
from models.user_model import UserModel
from models.ticket_model import TicketModel
from models.comment_model import CommentModel
from datetime import datetime

def seed_database():
    with db.session.begin():
        users = [
            {"username": "EclipseSupport_Pete", "password": "Eclipse@123!", "admin": True},
            {"username": "EclipseManager_Jack", "password": "Management#987", "admin": True},
            {"username": "EclipseSupport_Lucy", "password": "Support!678", "admin": True},
            {"username": "MediHire_John", "password": "Health#321!", "admin": False},
            {"username": "CareTalent_Sarah", "password": "CareRecruit@25", "admin": False},
            {"username": "HealthBridge_Mark", "password": "NurseXyz!", "admin": False},
            {"username": "BuildForce_Mike", "password": "Constuct123", "admin": False},
            {"username": "TradeSkills_Emma", "password": "TradeHire@2025", "admin": False},
            {"username": "EduTalent_Lisa", "password": "TeachHire456!", "admin": False},
            {"username": "UniHire_Daniel", "password": "UniRecruit@24", "admin": False}
        ]

        ticket_data = [
            {"title": "Issue with Login", "description": "User unable to log in after resetting password.", "priority": "High", "status": "Open", "author_id": 6, "assignee_id": 1},
            {"title": "Email Notifications Not Working", "description": "System fails to send confirmation emails after ticket creation.", "priority": "Medium", "status": "Pending", "author_id": 8, "assignee_id": 2},
            {"title": "Database Connection Issue", "description": "App crashes due to database connection timeout.", "priority": "Critical", "status": "In Progress", "author_id": 5, "assignee_id": 3},
            {"title": "UI Glitch on Mobile", "description": "Dropdown menus do not display properly on iOS devices.", "priority": "Low", "status": "Open", "author_id": 4, "assignee_id": 2},
            {"title": "Access Denied Error", "description": "Non-admin users can't access basic functionality.", "priority": "High", "status": "Resolved", "author_id": 5, "assignee_id": 3},
            {"title": "Integration Issue", "description": "Third-party API authentication failing after security update.", "priority": "Medium", "status": "Pending", "author_id": 6, "assignee_id": 1},
            {"title": "Server Downtime", "description": "Reports of intermittent server failures during peak hours.", "priority": "Critical", "status": "In Progress", "author_id": 7, "assignee_id": 2},
            {"title": "Ticket Assignment Bug", "description": "Tickets are not getting assigned correctly in admin dashboard.", "priority": "High", "status": "Open", "author_id": 8, "assignee_id": None},
            {"title": "Performance Lag", "description": "Page load times exceeding 5 seconds for larger datasets.", "priority": "Medium", "status": "In Progress", "author_id": 9, "assignee_id": 2},
            {"title": "User Profile Updates Not Saving", "description": "Changes made to user profiles are not persisting.", "priority": "Low", "status": "Open", "author_id": 10, "assignee_id": None}
        ]


        comment_data = [
            {"ticket_id": 1, "author_id": 1, "content": "This looks like a password caching issue. Can you clear saved credentials and try again?"},
            {"ticket_id": 1, "author_id": 6, "content": "I've cleared the saved credentials and tried again, I am still unable to log in."},
            {"ticket_id": 2, "author_id": 2, "content": "I've checked the email server logs—there's a delay in outgoing mail processing."},
            {"ticket_id": 3, "author_id": 3, "content": "I've confirmed that this is a database timeout."},
            {"ticket_id": 4, "author_id": 2, "content": "Confirmed: Mobile UI breaks on Safari. Will need a CSS fix."},
            {"ticket_id": 5, "author_id": 3, "content": "Can you please provide some additional clarification on the functionality non-admins cannot access."},
            {"ticket_id": 5, "author_id": 5, "content": "It's specifically the create candidate and create client functionality."},
            {"ticket_id": 6, "author_id": 1, "content": "Investigating API authentication logs now."},
            {"ticket_id": 7, "author_id": 2, "content": "Investigating downtime reported at peak hours. Could be a load balancing issue."},
            {"ticket_id": 9, "author_id": 2, "content": "Confirmed: High latency caused by large dataset queries."}
        ]


        for user_data in users:
            hashed_password = bcrypt.generate_password_hash(user_data["password"]).decode('utf-8')
            new_user = UserModel(username=user_data["username"], password=hashed_password, admin=user_data["admin"])
            db.session.add(new_user)

        for ticket in ticket_data:
            new_ticket = TicketModel(
                title=ticket["title"],
                description=ticket["description"],
                priority=ticket["priority"],
                status=ticket["status"],
                date_created=datetime.now(),
                date_updated=datetime.now(),
                author_id=ticket["author_id"],
                assignee_id=ticket["assignee_id"]
            )
            db.session.add(new_ticket)

        for comment in comment_data:
            new_comment = CommentModel(
                ticket_id=comment["ticket_id"],
                author_id=comment["author_id"],
                content=comment["content"],
                date_created=datetime.now(),
                date_updated=datetime.now()
            )
            db.session.add(new_comment)

    db.session.commit()
