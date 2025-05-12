from flask_login import UserMixin
from EclipseSupportPortal.__init__ import db

class UserModel(db.Model, UserMixin):
        __tablename__ = "user"
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), nullable=False, unique=True)
        password = db.Column(db.String(80), nullable=False)