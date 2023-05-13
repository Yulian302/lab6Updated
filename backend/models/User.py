from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),index=True,unique=True)
    password_hash = db.Column(db.String(128),index=False,unique=True)