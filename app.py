from flask import Flask, jsonify
import random
import time
from datetime import datetime

app = Flask(__name__)

# Função para gerar um ID de cheque digital com 16 dígitos
def generate_check_id():
    return ''.join([str(random.randint(0, 9)) for _ in range(16)])

# Endpoint para gerar um cheque digital
@app.route('/check/<credit_account_id>/ammount/<int:value>/', methods=['GET'])
def get_digital_check(credit_account_id, value):
    # Verifica se a conta de créditos é válida (apenas números de 16 dígitos)
    if len(credit_account_id) != 16 or not credit_account_id.isdigit():
        return jsonify({"error": "Invalid credit account ID. It must be a 16-digit number."}), 400
    
    # Gera a data e hora de emissão do cheque
    current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    
    # Gera o ID do cheque digital
    check_id = generate_check_id()
    
    # Criando o retorno JSON com os dados do cheque digital
    response = [{
        "date": current_time,
        "checkID": check_id
    }]
    
    return jsonify(response)

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)