from fastapi import APIRouter
from models.user import User 
from config.db import client 
from schemas.user import serializeDict, serializeList
from bson import ObjectId

user = APIRouter() 

@user.get('/')
async def Listar_todos_usuarios():
    return serializeList(client.local.user.find())


@user.post('/')
async def criar_usuario(user: User):
    client.local.user.insert_one(dict(user))
    return serializeList(client.local.user.find())

@user.put('/{id}')
async def atualizar_usuario(id,user: User):
    client.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(client.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def deletar_usuario(id,user: User):
    return serializeDict(client.local.user.find_one_and_delete({"_id":ObjectId(id)}))

