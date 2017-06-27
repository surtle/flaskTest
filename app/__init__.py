from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager, UserMixin, login_user, logout_user, \
       current_user
from oauth import OAuthSignIn

# initialize app
app = Flask(__name__)
app.config.from_object('config')

app.config['SECRET_KEY'] = 'woahthere'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['OAUTH_CREDENTIALS'] = {
  'facebook': {
    'id': '470154729788964',
    'secret': '010cc08bd4f51e34f3f3e684fbdea8a7'
  }
}

# initialize database
db = SQLAlchemy(app)
db.create_all()

from app import views
