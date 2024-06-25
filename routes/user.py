from fastapi import APIRouter
from models.user import User 
from config.db import client 
from schemas.user import serializeDict, serializeList
from bson import ObjectId

user = APIRouter() 

@user.get('/api/listar')
async def Listar_todos_usuarios():
    '''
    Endpoint que exibe a lista de todos os usuarios
    '''
    return serializeList(client.local.user.find())


@user.post('/api/criar')
async def criar_usuario(user: User):
    '''
    Endpoint que cria todos os usuarios 
    '''
    client.local.user.insert_one(dict(user))
    return serializeList(client.local.user.find())

@user.put('/api/atualizar/{id}')
async def atualizar_usuario(id,user: User):
    '''
    Endpoint que atualiza algum usuario pelo id
    '''
    client.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(client.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/api/deleletar/{id}')
async def deletar_usuario(id,user: User):
    '''
    Endponit que deleta algum usuario pelo id
    '''
    return serializeDict(client.local.user.find_one_and_delete({"_id":ObjectId(id)}))

