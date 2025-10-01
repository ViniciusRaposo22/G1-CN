import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Caminho para armazenar as mensagens
messages_file = '/app/data/messages.json'

# Função para ler as mensagens do arquivo
def read_messages():
    if os.path.exists(messages_file):
        with open(messages_file, 'r') as f:
            return json.load(f)
    else:
        return [] 

# Função para salvar as mensagens no arquivo
def save_message(message):
    messages = read_messages()
    messages.append(message)
    
    with open(messages_file, 'w') as f:
        json.dump(messages, f)

@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({'error': 'Mensagem não fornecida ou corpo da requisição inválido'}), 400

        save_message(data['message'])
        return jsonify({'message': 'Mensagem recebida com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro ao processar a mensagem: {str(e)}'}), 500

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify({'mensagens': read_messages()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)