# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprenda a criar APIs RESTful com o framework FastAPI em Python. Nesta tarefa você irá definir modelos com Pydantic, implementar endpoints CRUD, validar entradas, e expor documentação automática (Swagger/OpenAPI).

## 📝 Tasks

### 🛠️	Implementar uma API REST básica

#### Description
Crie uma pequena API que gerencie recursos do tipo `Item` (ou similar) usando FastAPI. A API deve suportar operações CRUD (Create, Read, Update, Delete), validar dados de entrada com modelos Pydantic e retornar respostas apropriadas com códigos HTTP corretos.

#### Requirements
Completed program should:

- Fornecer endpoints HTTP para: listar todos os itens (`GET /items`), obter um item (`GET /items/{id}`), criar um item (`POST /items`), atualizar um item (`PUT /items/{id}`) e excluir um item (`DELETE /items/{id}`).
- Usar modelos Pydantic para validação de entrada e serialização de saída.
- Retornar códigos de status HTTP apropriados (por exemplo, `201 Created` ao criar, `404 Not Found` quando o item não existir).
- Armazenar dados em uma estrutura em memória (por exemplo, `dict`) — não é necessário banco de dados para esta tarefa.
- Expor documentação automática (Swagger UI) disponível em `/docs` e OpenAPI em `/openapi.json`.
- Incluir instruções de execução no arquivo `README.md` e um `starter-code.py` funcional que inicie o servidor com `uvicorn`.

Exemplo de uso (resumido):

```
# criar um item
POST /items
{
  "name": "Caneca",
  "price": 12.5
}

# resposta: 201 Created
```


### 🛠️	Extras (opcional)

#### Description
Funcionalidades opcionais para aprofundar conhecimentos e tornar a API mais completa.

#### Requirements
Completed program may include one or more of the following:

- Persistência em banco de dados leve (SQLite) usando `SQLModel` ou `SQLAlchemy`.
- Adição de autenticação simples (por exemplo, API key ou token) para proteger endpoints de escrita.
- Testes automáticos para os endpoints (usando `pytest` e `httpx`/`TestClient`).
- Dockerfile para empacotar a aplicação e `docker-compose` com serviço de banco (se usado).

---

## Como rodar (exemplo rápido)

1. Criar um ambiente virtual e instalar dependências:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Iniciar a API (modo desenvolvimento):

```
uvicorn starter_code:app --reload
```

3. Abrir `http://localhost:8000/docs` para ver a documentação interativa.
