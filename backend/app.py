from flask import Flask
from flask_login import LoginManager,login_required,login_user,logout_user
from werkzeug.security import check_password_hash,generate_password_hash
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_migrate import Migrate

app = Flask(__name__)

# postgres credentials

DB_USERNAME = environ.get('DB_USERNAME')
DB_PASSWORD = environ.get('DB_PASSWORD')
DB_NAME = environ.get('DB_NAME')
DB_HOST = environ.get('DB_HOST')
DB_PORT = environ.get('DB_PORT')
DB_DRIVER = 'psycopg2'
# app config

app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql+{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
# db connection
db = SQLAlchemy(app)
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
migrate = Migrate(app,db)

import models.Product
import routes.rest_routes
# if __name__=='__main__':
#     app.run(debug=True)

