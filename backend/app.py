from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS

app = Flask(__name__)

# postgres credentials

DB_USERNAME = environ.get('DB_USERNAME')
DB_PASSWORD = environ.get('DB_PASSWORD')
DB_NAME = environ.get('DB_NAME')
DB_HOST = environ.get('DB_HOST')
DB_PORT = environ.get('DB_PORT')
DB_DRIVER = 'psycopg2'

# login manager
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view='/login'

# app config
app.secret_key = "sOmEseCrEt6key"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


# jwt
app.config['JWT_SECRET_KEY'] = 'neo_bruno_secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)

# db connection
db = SQLAlchemy(app)
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
migrate = Migrate(app, db)
import routes.rest_routes
import models.Product
# blueprints
from routes.rest_routes import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# if __name__=='__main__':
#     app.run(debug=True)
