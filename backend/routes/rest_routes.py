from app import app
from flask import redirect,url_for
from models.Product import Product
from flask import jsonify

@app.route('/')
def initial():
    return redirect(url_for('home',__external=True))

@app.route('/home')
def home():
    products = Product.query.all()
    return jsonify([{'id':product.id,'name':product.name,'price':product.price,'img_url':product.img_url,'description':product.description} for product in products])