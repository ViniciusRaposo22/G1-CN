from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

caminho_arquivo = '/data/mensagens.txt'

def salvar_mensagem(mensagem):
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(mensagem + '\n')

def obter_mensagens():
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r') as arquivo:
            return arquivo.readlines()
    return []

def enviar_containers(mensagem):
    containers = [
        'http://app2:5000/send',
        'http://app3:5000/send' 
    ]
    for container in containers:
        try:
            resposta = requests.post(container, json={"message": mensagem})
            if resposta.status_code == 201:
                print(f"Mensagem enviada para {container}")
        except requests.exceptions.RequestException as erro:
            print(f"Falha ao enviar mensagem para {container}: {erro}")

@app.route('/send', methods=['POST'])
def receber_mensagem():
    dados = request.get_json()
    mensagem = dados.get('message')
    
    if mensagem:
        salvar_mensagem(mensagem)

        enviar_containers(mensagem)

        return jsonify({"status": "Mensagem recebida", "message": mensagem}), 201
    else:
        return jsonify({"erro": "Nenhuma mensagem fornecida"}), 400

@app.route('/messages', methods=['GET'])
def listar_mensagens():
    mensagens = obter_mensagens()
    return jsonify({"mensagens": mensagens})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
