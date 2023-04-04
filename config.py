from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
print("os.getenv('DB_URI') os.getenv('DB_URI') : ", os.getenv('DB_URI'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
