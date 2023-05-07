from sys import path
from os.path import abspath,join,dirname

path.append(abspath(join(dirname(__file__),'..')))

from app import db

class Product(db.Model):
    __tablename__='product'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),index=True,unique=False,nullable=False)
    price = db.Column(db.Integer,index=False,unique=False,nullable=False)
    img_url = db.Column(db.String(255),index=True,unique=True,nullable=True)
    description = db.Column(db.String(200),index=True,unique=False,nullable=False)

    def __init__(self,name,price,img_url,description):
        self.name = name
        self.price = price
        self.img_url = img_url
        self.description = description

    def __repr__(self):
        return '<Product %r>' % (self.name)
