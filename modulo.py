from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

app.secret_key = 'Something_Secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)