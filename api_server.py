from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import List
from datetime import date

app = FastAPI()

# Configuração do MongoDB usando PyMongo

MONGO_URI=""
client = MongoClient(MONGO_URI)
db = client['rolezinhos']
bares_collection = db['bares']
users_collection = db['users']

# Modelos Pydantic para os dados do Bar e User
class GPS(BaseModel):
    type: str
    coordinates: List[float]

class Bar(BaseModel):
    nome: str
    endereco: str
    descricao: str
    gps: GPS

class User(BaseModel):
    nome: str
    data_nascimento: date

# Função para converter ObjectId para string
def bar_serializer(bar) -> dict:
    return {
        "id": str(bar["_id"]),
        "nome": bar["nome"],
        "endereco": bar["endereco"],
        "descricao": bar["descricao"],
        "gps": bar["gps"]
    }

def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "nome": user["nome"],
        "data_nascimento": user["data_nascimento"]
    }

# CRUD para Bares

# Criar um único bar
@app.post("/bares/novo", response_model=dict)
def criar_bar(bar: Bar):
    insercao = bares_collection.insert_one(bar.dict())
    return {"inserted_id": str(insercao.inserted_id)}

# Ler todos os bares
@app.get("/bares/", response_model=List[dict])
def ler_bares():
    bares = bares_collection.find()
    return [bar_serializer(bar) for bar in bares]

# Ler um bar pelo ID
@app.get("/bares/{bar_id}", response_model=dict)
def ler_bar(bar_id: str):
    bar = bares_collection.find_one({"_id": ObjectId(bar_id)})
    if bar:
        return bar_serializer(bar)
    raise HTTPException(status_code=404, detail="Bar não encontrado")

# Atualizar um bar pelo ID
@app.put("/bares/{bar_id}", response_model=dict)
def atualizar_bar(bar_id: str, bar: Bar):
    resultado = bares_collection.update_one(
        {"_id": ObjectId(bar_id)}, {"$set": bar.dict()}
    )
    if resultado.modified_count:
        return {"msg": "Bar atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Bar não encontrado")

# Deletar um bar pelo ID
@app.delete("/bares/{bar_id}", response_model=dict)
def deletar_bar(bar_id: str):
    resultado = bares_collection.delete_one({"_id": ObjectId(bar_id)})
    if resultado.deleted_count:
        return {"msg": "Bar deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Bar não encontrado")

# CRUD para Users

# Criar um único usuário
@app.post("/users/novo", response_model=dict)
def criar_user(user: User):
    insercao = users_collection.insert_one(user.dict())
    return {"inserted_id": str(insercao.inserted_id)}

# Ler todos os usuários
@app.get("/users/", response_model=List[dict])
def ler_users():
    users = users_collection.find()
    return [user_serializer(user) for user in users]

# Ler um usuário pelo ID
@app.get("/users/{user_id}", response_model=dict)
def ler_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_serializer(user)
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Atualizar um usuário pelo ID
@app.put("/users/{user_id}", response_model=dict)
def atualizar_user(user_id: str, user: User):
    resultado = users_collection.update_one(
        {"_id": ObjectId(user_id)}, {"$set": user.dict()}
    )
    if resultado.modified_count:
        return {"msg": "Usuário atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Deletar um usuário pelo ID
@app.delete("/users/{user_id}", response_model=dict)
def deletar_user(user_id: str):
    resultado = users_collection.delete_one({"_id": ObjectId(user_id)})
    if resultado.deleted_count:
        return {"msg": "Usuário deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


