from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.middleware.cors import CORSMiddleware

from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from api import secret
import uvicorn


app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.get("/")
async def root():
    with open("README.md", "r") as f:
        readme_contents = f.read()
    return {"message": readme_contents}


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
async def get_task(task_id: int, user: str = Security(get_current_user)):
    task = mongo_collection.find_one({"id": task_id})
    if task:
        return task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.put("/api/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task, user: str = Security(get_current_user)):
    task_data = task.dict()
    updated_task = mongo_collection.find_one_and_update(
        {"id": task_id},
        {"$set": task_data},
        return_document=True
    )
    if updated_task:
        return updated_task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.delete("/api/{task_id}", response_model=Task)
async def delete_task(task_id: int, user: str = Security(get_current_user)):
    deleted_task = mongo_collection.find_one_and_delete({"id": task_id})
    if deleted_task:
        return deleted_task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


def clearDB():
    mongo_collection.delete_many({})
    print("Banco de dados limpo!")
#clearDB()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
