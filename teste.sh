#!/bin/bash

# Enviar uma mensagem para o app1
echo "Enviando mensagem para app1..."
curl -X POST -H "Content-Type: application/json" -d '{"message":"Olá do app1"}' http://localhost:5001/send

# Verificar as mensagens em todos os containers
echo "Verificando as mensagens no app1..."
curl http://localhost:5001/messages

echo "Verificando as mensagens no app2..."
curl http://localhost:5002/messages

echo "Verificando as mensagens no app3..."
curl http://localhost:5003/messages

# Enviar mensagem para o app2
echo "Enviando mensagem para app2..."
curl -X POST -H "Content-Type: application/json" -d '{"message":"Olá do app2"}' http://localhost:5002/send

# Verificar as mensagens em todos os containers
echo "Verificando as mensagens no app1..."
curl http://localhost:5001/messages

echo "Verificando as mensagens no app2..."
curl http://localhost:5002/messages

echo "Verificando as mensagens no app3..."
curl http://localhost:5003/messages
