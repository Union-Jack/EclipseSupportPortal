from extensions import db
from datetime import datetime


class TicketModel(db.Model):
    __tablename__ = "ticket"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(10), default='Normal')
    status = db.Column(db.String(10), default='Open')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    comments = db.relationship('CommentModel', backref='ticket', lazy='dynamic', cascade='all, delete-orphan')

