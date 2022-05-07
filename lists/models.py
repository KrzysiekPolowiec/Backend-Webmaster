from cgitb import enable
from lists import db

class Lists (db.Model): #tabela bazy danych dla lists
    id=db.column(db.Integer(), primary_key=True)
    name=db.column(db.String(length=50), nullable=False)
    lista = db.relationship('List', backref='owned_suer', lazy=True)

class List(db.Model): #tabela bazy danych dla itemów np. jajka, mleko ,cola
    id=db.column(db.Integer(), primary_key=True)
    name=db.column(db.String(length=50), nullable=False)
    amount=db.column(db.Integer(), nullable=False)
    pucharsed=db.column(db.Boolean(), deafult=False)
    owner=db.column(db.Integer(), db.ForeginKey('lists.id')) #klucz obcy z tabeli wyżej

    def __repr__ (self):
        return f'List {self.name}'