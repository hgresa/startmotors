from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app._static_folder = 'templates/static'
db = SQLAlchemy(app)
config = Config()

app.config['SECRET_KEY'] = 'nomc1589z'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'

from app.controllers.inventory_management_routes import Product, ProductHistory, Car, EAV
from app.controllers import CompletedWork, Employee, Expense, Payment, Salary, Main, Statistics
