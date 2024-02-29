!pip install flask

!pip instal pandas

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# URL da planilha no OneDrive
planilha_url = "https://1drv.ms/x/s!Am5FFtj4Ioa9gpRPCRHFBI7fFniDow?e=FkPay4"

# Rota principal
@app.route('/index')
def index():
    # Lê a planilha do Excel
    try:
        df = pd.read_excel(planilha_url)
        # Converte o DataFrame para formato JSON
        json_data = df.to_json(orient='records')
        return jsonify(json_data)
    except Exception as e:
        return f"Erro ao ler a planilha: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)