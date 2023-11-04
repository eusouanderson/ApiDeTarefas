# API de Tarefas

Uma API simples para criar, listar, buscar, atualizar e excluir tarefas. É necessária autenticação para acessar essas funcionalidades.

## Tecnologias Utilizadas

- **FastAPI:** Framework web utilizado para criar a API.
- **MongoDB:** Banco de dados NoSQL utilizado para armazenar as tarefas.
- **Uvicorn:** Servidor ASGI utilizado para executar o aplicativo FastAPI.


## Configuração

Para usar esta API, você deve fornecer autenticação. Use o seguinte username e password para autenticação básica:

- Username: `{{ADMIN_USERNAME}}`
- Password: `{{ADMIN_PASSWORD}}`

## Endpoints

### Autenticação

- **POST /token:** Rota para obter um token de autenticação. Você deve fornecer o username e password no corpo da solicitação.

### Criar Tarefa

- **POST /api/:** Rota para criar uma nova tarefa.

    Exemplo de solicitação:
    ```json
    {
        "title": "Nova tarefa",
        "description": "Nova descrição"
    }
    ```

### Listar Tarefas

- **GET /api/:** Rota para obter todas as tarefas.

### Obter Tarefa por ID

- **GET /api/{task_id}:** Rota para obter uma tarefa pelo seu ID.

    Exemplo:
    ```
    GET /api/123
    ```

### Atualizar Tarefa por ID

- **PUT /api/{task_id}:** Rota para atualizar uma tarefa pelo seu ID.

    Exemplo de solicitação:
    ```json
    {
        "title": "Nova tarefa, depois",
        "description": "Nova descrição"
    }
    ```

### Deletar Tarefa por ID

- **DELETE /api/{task_id}:** Rota para excluir uma tarefa pelo seu ID.

## Exemplos de Uso

Aqui estão alguns exemplos de como usar a API com `curl`:

1. Autenticar e obter um token:
   ```bash
   curl -X POST -d "username={{ADMIN_USERNAME}}" -d "password={{ADMIN_PASSWORD}}" http://localhost:8000/token


2. Criar uma tarefa:

    ```bash

    curl -X POST -H "Authorization: Bearer {TOKEN}" -d '{"title": "Nova tarefa", "description": "Nova descrição"}' http://localhost:8000/api/

    
3. Listar todas as tarefas

      ```bash
      curl -H "Authorization: Bearer {TOKEN}" http://localhost:8000/api/
      
4. Obter uma tarefa por ID:
    
    ```bash
    curl -H "Authorization: Bearer {TOKEN}" http://localhost:8000/api/{task_id}

5. Atualizar uma tarefa por ID:

    ```bash
    curl -X PUT -H "Authorization: Bearer {TOKEN}" -d '{"title": "Nova tarefa, depois", "description": "Nova descrição"}' http://localhost:8000/api/{task_id}

## Executar a Api 

Você pode executar o aplicativo usando Uvicorn. Use o seguinte comando para iniciar o servidor:

    
    uvicorn main:app --host 127.0.0.1 --port 8000
    
    
Lembre-se de substituir {{ADMIN_USERNAME}} e {{ADMIN_PASSWORD}} pelos valores reais do seu aplicativo.

    
    Certifique-se de substituir `{{ADMIN_USERNAME}}` e `{{ADMIN_PASSWORD}}` pelos valores reais do seu aplicativo antes de adicionar esta documentação ao seu repositório GitHub. Isso ajudará os usuários a entender como usar sua API.



