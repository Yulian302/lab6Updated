from app import db,app
from models.Product import Product

product1 = Product(name='fsdfd',price=323,img_url='23432',description='fsdsdfdfs')

with app.app_context():
    db.session.add(product1)
    db.session.commit()