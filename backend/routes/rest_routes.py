from app import app, db
from flask import redirect, url_for, jsonify, request
from models.Product import Product
from models.User import User
from flask import Blueprint
from flask_jwt_extended import create_access_token, unset_jwt_cookies, get_jwt, get_jwt_identity, jwt_required
from json import dumps
from datetime import datetime, timedelta
from datetime import timezone
import bcrypt


auth = Blueprint('auth', __name__)


@app.route('/')
def initial():
    return redirect(url_for('home', __external=True))


@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'password_hash': user.password_hash} for user in users])


@auth.route('/token', methods=["POST"])
def create_token():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        return {'msg': 'Wrong username or password'}, 401
    access_token = create_access_token(identity=username)
    response = {'access_token': access_token}
    return response


@auth.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token
                response.data = dumps(data)
        return response
    except (RuntimeError, KeyError):
        return response


@auth.route('/logout', methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successfull"})
    unset_jwt_cookies(response)
    return response


@app.route('/home')
@jwt_required()
def home():
    current_username = get_jwt_identity()
    user = User.query.filter_by(username=current_username).first()
    response_body = {
        "username": user.username
    }
    products = Product.query.all()
    return jsonify([{'id': product.id, 'name': product.name, 'price': product.price, 'img_url': product.img_url, 'description': product.description, 'category': product.category} for product in products])


@auth.route('/signup', methods=["POST"])
def signup():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not User.query.filter_by(username=username).first():
        user = User(username=username, password_hash=password)
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({"msg": "User created successfully"})
        except:
            db.session.rollback()
    else:
        return jsonify({"error": "Username already exists"}), 400
