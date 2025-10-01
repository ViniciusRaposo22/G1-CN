#!/bin/bash

# Testando a criação de uma mensagem
echo "Enviando mensagem para app1"
curl -X POST -H "Content-Type: application/json" -d '{"message":"Ola do app1"}' http://localhost:5001/send

# Verificando se as mensagens foram armazenadas no app1
echo "Verificando mensagens em app1"
curl http://localhost:5001/messages

# Verificando se a replicação foi feita corretamente em app2 e app3
echo "Verificando mensagens em app2"
curl http://localhost:5002/messages

echo "Verificando mensagens em app3"
curl http://localhost:5003/messages
