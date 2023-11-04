from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from api import secret

app = FastAPI()

# Configuração da autenticação básica (usuário e senha)
ADMIN_PASSWORD = secret.PASSWORD
ADMIN_USERNAME = secret.USERNAME

# Configuração do MongoDB
mongo_client = MongoClient(f"mongodb+srv://{secret.USERNAME}:{secret.PASSWORD}@cluster0.t1exjft.mongodb.net/")
mongo_db = mongo_client["tasks"]
mongo_collection = mongo_db["tasks"]

# Contador para ID das tarefas
task_id_counter = 1

# Definição da estrutura da tarefa
class Task(BaseModel):
    id: int = None
    title: str
    description: str

# Rota para autenticação
auth_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Função para verificar a autenticação do usuário
async def get_current_user(token: str = Depends(auth_scheme)):
    if token != f"{ADMIN_USERNAME}:{ADMIN_PASSWORD}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return token

@app.options("/token", response_model=str)
async def login():
    return f"{ADMIN_USERNAME}:{ADMIN_PASSWORD}"


@app.post("/api/", response_model=Task)
async def create_task(task: Task, user: str = Security(get_current_user)):
    """ 
    Rota para criar uma tarefa
    Exemplo: post /api/ --data '{"title": "Nova tarefa", "description": "Nova descricão"}'
    """
    global task_id_counter
    task_data = task.dict()
    task_data["id"] = task_id_counter
    inserted_task = mongo_collection.insert_one(task_data)
    task_id_counter += 1
    task.id = task_data["id"]
    return task


@app.get("/api/", response_model=list[Task])
async def get_tasks(user: str = Security(get_current_user)):
    """
    Rota para obter todas as tarefas
    Exemplo: get /api/
    """
    tasks = list(mongo_collection.find({}))
    return tasks


@app.get("/api/{task_id}", response_model=Task)
async def get_task(task_id: str, user: str = Security(get_current_user)):
    """
    Rota para obter uma tarefa pelo seu ID
    Exemplo: get /api/123
    """
    task = mongo_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        task["id"] = task_id
        return task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.put("/api/{task_id}", response_model=Task)
async def update_task(task_id: str, task: Task, user: str = Security(get_current_user)):
    """
    Rota para atualizar uma tarefa pelo seu ID
    Exemplo: put /api/123 --data '{"title": "Nova tarefa, depois", "description": "Nova descricão"}'
    """
    task_data = task.dict()
    updated_task = mongo_collection.find_one_and_update(
        {"_id": ObjectId(task_id)},
        {"$set": task_data},
        return_document=True
    )
    if updated_task:
        updated_task["id"] = task_id
        return updated_task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.delete("/api/{task_id}", response_model=Task)
async def delete_task(task_id: str, user: str = Security(get_current_user)):
    """
    Rota para deletar uma tarefa pelo seu ID
    Exemplo: delete /api/123
    """
    deleted_task = mongo_collection.find_one_and_delete({"_id": ObjectId(task_id)})
    if deleted_task:
        deleted_task["id"] = task_id
        return deleted_task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


def clearDB():
    mongo_collection.delete_many({})
    print("Banco de dados limpo!")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
