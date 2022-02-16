from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "fortheloveofgodchangethis"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


login_manager = LoginManager()
login_manager.init_app(app)


from dta_pkt import models, forms, routes
