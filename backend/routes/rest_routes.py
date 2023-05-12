from app import app,login_manager
from flask_login import login_required
from flask import redirect,url_for,jsonify
from models.Product import Product
from models.User import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def initial():
    return redirect(url_for('home',__external=True))

@app.route('/home')
@login_required
def home():
    products = Product.query.all()
    return jsonify([{'id':product.id,'name':product.name,'price':product.price,'img_url':product.img_url,'description':product.description,'category':product.category} for product in products])


@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{'id':user.id,'username':user.username,'password_hash':user.password_hash} for user in users])