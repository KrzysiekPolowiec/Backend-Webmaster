from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqllite:///lists.db' # konfiguracja bazy danych
db = SQLAlchemy(app)

from lists import routes
