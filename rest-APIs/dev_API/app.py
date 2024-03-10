from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Desenvolvedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    habilidades = db.Column(db.String(200), nullable=False)

# Rota para listar todos os desenvolvedores
@app.route('/dev/', methods=['GET'])
def lista_desenvolvedores():
    desenvolvedores = Desenvolvedor.query.all()
    return jsonify([dev.to_dict() for dev in desenvolvedores])

# Rota para obter um desenvolvedor por ID
@app.route('/dev/<int:id>/', methods=['GET'])
def desenvolvedor(id):
    desenvolvedor = Desenvolvedor.query.get_or_404(id)
    return jsonify(desenvolvedor.to_dict())

# Rota para adicionar um novo desenvolvedor
@app.route('/dev/', methods=['POST'])
def novo_desenvolvedor():
    dados = request.get_json()
    novo_dev = Desenvolvedor(nome=dados['nome'], habilidades=dados['habilidades'])
    db.session.add(novo_dev)
    db.session.commit()
    return jsonify(novo_dev.to_dict())

# Rota para atualizar um desenvolvedor por ID
@app.route('/dev/<int:id>/', methods=['PUT'])
def atualizar_desenvolvedor(id):
    desenvolvedor = Desenvolvedor.query.get_or_404(id)
    dados = request.get_json()
    desenvolvedor.nome = dados['nome']
    desenvolvedor.habilidades = dados['habilidades']
    db.session.commit()
    return jsonify(desenvolvedor.to_dict())

# Rota para remover um desenvolvedor por ID
@app.route('/dev/<int:id>/', methods=['DELETE'])
def remover_desenvolvedor(id):
    desenvolvedor = Desenvolvedor.query.get_or_404(id)
    db.session.delete(desenvolvedor)
    db.session.commit()
    return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})

# Cria as tabelas do banco de dados
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

# Classe para serializar os dados do desenvolvedor
class ModelToJson:
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'habilidades': self.habilidades.split(',')
        }