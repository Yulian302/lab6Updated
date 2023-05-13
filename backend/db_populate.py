from app import db,app
from models.Product import Product
from models.User import User
from werkzeug.security import generate_password_hash

user1 = User(username='Yulian302',password_hash=generate_password_hash('3022003bu'))

with app.app_context():
    db.session.add(user1)
    db.session.commit()