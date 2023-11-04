from pymongo import MongoClient
from api import secret


# Conecte-se ao MongoDB
client = MongoClient("mongodb://localhost:27017")
def clearDB():
# Selecione o banco de dados e a coleção
  db = client["meu_banco_de_dados"]
  colecao = db["minha_colecao"]

# Defina um filtro para identificar o documento que você deseja apagar
  filtro = {"task": "valor_chave"}

# Apague o documento que corresponde ao filtro
  colecao.delete_one(filtro)
