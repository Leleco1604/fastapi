from pydantic import BaseModel

class User(BaseModel):
    nome: str
    email: str
    data_nascimento: str
    senha: str