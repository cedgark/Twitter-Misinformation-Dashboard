from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f5ac4a5b01e230dee6aebfd6d6d4bca3992424f24e353439'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2064607:Groupwork123@csmysql.cs.cf.ac.uk:3306/c2064607_CM2305_Group_Project'

db = SQLAlchemy(app)

from dashboard import routes
from dashboard.models import Emotions, Hashtags, Locations, Mentions, Trends, Tweetids, Wordcloud, States, Coords
