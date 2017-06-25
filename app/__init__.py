from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

# initialize app
app = Flask(__name__)
app.config.from_object('config')

# initialize database
db = SQLAlchemy(app)

from app import views
