from app import app
from models import db, Admin, Cliente


with app.app_context():
    # Só cria as tabelas se não existirem
    db.create_all()

    # Criar admin e cliente teste
    admin = Admin(cpf='admin', email='admin@admin')
    cliente = Cliente(nome='123',telefone='123456789',cpf='1234', email='123@123')

    db.session.add(admin)
    db.session.add(cliente)
    db.session.commit()