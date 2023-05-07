from app import app
from flask import redirect,url_for

@app.route('/')
def initial():
    return redirect(url_for('home',__external=True))

@app.route('/home')
def home(): 
    return 'home'