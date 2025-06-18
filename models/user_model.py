from flask_login import UserMixin
from extensions import db
from datetime import datetime
from models.comment_model import CommentModel

#Represents the user table in the database
class UserModel(db.Model, UserMixin):
        __tablename__ = "user"
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), nullable=False, unique=True)
        password = db.Column(db.String(80), nullable=False)
        admin = db.Column(db.Boolean, nullable=False, default=False)
        date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
        date_updated = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
        tickets_created = db.relationship('TicketModel', backref='author', lazy='dynamic', foreign_keys='TicketModel.author_id')
        tickets_assigned = db.relationship('TicketModel', backref='assignee', lazy='dynamic', foreign_keys='TicketModel.assignee_id')
        comments = db.relationship('CommentModel', backref='author', lazy='dynamic')
        
