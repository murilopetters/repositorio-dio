from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/<int:id>')
def pessoa(id):
    soma = 1 + id
    return jsonify({'id': id, 'nome': 'Cezar', 'idade': '33'})


@app.routa('/soma', methods=['POST'])
def soma():
    if request.method == 'POST'
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify{'soma': total}


if __name__ == '__main__':
    app.run(debug=True)