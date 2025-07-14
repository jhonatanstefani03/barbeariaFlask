from flask import Flask,render_template,request
from flask import Flask, render_template, request, redirect, url_for
from models import db, Cliente, Admin, Barbeiro, create_tables

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  


@app.route('/')
def index():
    return  render_template('index.html')


@app.route('/cliente', methods=['POST'])
def cliente():
    cpf = request.form.get('cpf', '').strip()
    email = request.form.get('email', '').strip().lower()
    cliente = Cliente.query.filter_by(cpf=cpf, email=email).first()
    admin = Admin.query.filter_by(cpf=cpf, email=email).first()
    if cliente:
        return render_template('cliente.html')
    elif admin:
        return render_template('admin.html')
    else:
        return 'Cliente ou admin não encontrado', 404

@app.route('/admin')
def admin_painel():
    return render_template('admin.html')

#------------------------cadastros-----------------------------------------
@app.route('/cadastro_clientes', methods=['GET', 'POST'])
def cadastrar_cliente():
    mensagem = None
    erro = None

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        cpf = request.form.get('cpf', '').strip()
        telefone = request.form.get('telefone', '').strip()
        email = request.form.get('email', '').strip().lower()

        cliente_existente = Cliente.query.filter(
            (Cliente.cpf == cpf) | (Cliente.telefone == telefone) | (Cliente.email == email)
        ).first()

        if cliente_existente:
            erro = 'CPF, telefone ou email já cadastrados!'
        else:
            novo_cliente = Cliente(
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                email=email
            )
            db.session.add(novo_cliente)
            db.session.commit()
            mensagem = 'Cliente cadastrado com sucesso!'

    clientes = Cliente.query.all()
    return render_template('admin/cadastro_clientes.html', mensagem=mensagem, erro=erro, clientes=clientes)



@app.route('/cadastrar_barbeiro', methods=['GET', 'POST'])
def cadastrar_barbeiro():
    mensagem = None
    erro = None

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        cpf = request.form.get('cpf', '').strip()
        telefone = request.form.get('telefone', '').strip()
        especialidade = request.form.get('especialidade', '').strip()

        barbeiro_existente = Barbeiro.query.filter(
            (Barbeiro.cpf == cpf) | (Barbeiro.telefone == telefone)
        ).first()

        if barbeiro_existente:
            erro = 'CPF ou telefone já cadastrados!'
        else:
            novo_barbeiro = Barbeiro(
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                especialidade=especialidade
            )
            db.session.add(novo_barbeiro)
            db.session.commit()
            mensagem = 'Barbeiro cadastrado com sucesso!'

    barbeiros = Barbeiro.query.all()
    return render_template('admin/cadastro_barbeiros.html', mensagem=mensagem, erro=erro, barbeiros=barbeiros)

#------------------------END_CADASTRO----------------------------

@app.route('/remover_cliente/<int:id>', methods=['POST'])
def remover_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('cadastrar_cliente'))


@app.route('/remover_barbeiro/<int:id>', methods=['POST'])
def remover_barbeiro(id):
    barbeiro = Barbeiro.query.get_or_404(id)
    db.session.delete(barbeiro)
    db.session.commit()
    return redirect(url_for('cadastrar_barbeiro'))




@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')








if __name__ =='__main__':
    app.run(debug=True)