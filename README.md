# Sistema de Mensagens Distribuídas com Docker e Flask

Este projeto implementa um sistema de mensagens distribuídas usando **Docker**, **Docker Compose** e **Flask**. A aplicação consiste em três instâncias do serviço, onde cada uma pode enviar e receber mensagens de forma distribuída e persistente usando volumes compartilhados.

## Requisitos

Antes de iniciar, verifique se você tem as seguintes ferramentas instaladas em sua máquina:

- **Docker**
- **Docker Compose**

## Estrutura do Projeto

```plaintext
/G1 - CN/
├── app/
│ ├── app.py 
│ ├── requirements.txt
│ └── Dockerfile
├── docker-compose.yml
├── test.sh
└── README.md
```

## Passo a Passo para Executar a Aplicação
### 1. Clonar o repositório
    git clone <URL_DO_REPOSITORIO>
    cd <CAMINHO_PARA_ARQUIVO>

### 2.Construir e subir os containers
    docker-compose up --build -d

Este comando irá:
- Construir as imagens Docker usando o Dockerfile.
- Subir três instâncias do serviço Flask (app1, app2, app3).
- Criar um volume compartilhado para persistir as mensagens.

### 3.Executar o script de teste
    cd <CAMINHO_PARA_ARQUIVO>
    ./teste.sh

### 4.Executar testes manuais (Opcional)
    curl -X POST -H "Content-Type: application/json" -d '{"message":"Ola do app1"}' http://localhost:5001/send
    curl -X POST -H "Content-Type: application/json" -d '{"message":"Ola do app2"}' http://localhost:5002/send
    curl -X POST -H "Content-Type: application/json" -d '{"message":"Ola do app3"}' http://localhost:5003/send

Resposta esperada:
{"message":"Mensagem recebida com sucesso!"}

### 5.Verifique a mensagens salvas no volume (Opcional)
    curl http://localhost:5001/messages
    curl http://localhost:5002/messages
    curl http://localhost:5003/messages

As repostas devem ser iguais.