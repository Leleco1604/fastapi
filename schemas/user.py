# Normal way
def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "nome":item["nome"],
        "data_nascimento": item ["data_nascimento"],
        "email":item["email"],
        "senha":item["senha"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
    

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

# {i:str(a[i]) for i in a if i=='_id'} 
#Cria um dicionário que converte o valor do campo _id em uma string.
#MongoDB usa ObjectId para o campo _id,e isso garante que _id seja convertido de ObjectId para str.

#{i:a[i] for i in a if i!='_id'}
#Cria um dicionário com todos os outros campos que não sejam _id, mantendo seus valores inalterados.


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]

# itera sobre cada item em entity (que é uma lista de documentos), aplicando a função serializeDict a cada item.

