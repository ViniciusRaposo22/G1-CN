## Estrutura do Projeto

```
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
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd "G1 - CN"
    ```
### 2.Construir e subir os containers
    ```bash
    docker-compose up --build
    ```
### 3.Executar o script de teste
    ```bash
    chmod +x test.sh
    ./test.sh
    ```