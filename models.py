from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(100),nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    telefone= db.Column(db.String(50),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Barbeiro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    telefone= db.Column(db.String(50),unique=True,nullable=False)
    especialidade = db.Column(db.String(100))

def create_tables(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()