from pymongo import MongoClient

client = MongoClient()

db = client.local

# Criando coleções e inserir dados iniciais
def create_collections():
    # Coleção 'user'
    if 'user' not in db.list_collection_names():
        user_collection = db.create_collection('user')
        user_collection.insert_many([
            {
                "nome": "João Silva",
                "email": "joao.silva@example.com",
                "data_nascimento": "1990-01-01",
                "senha": "senha123"
            },
            {
                "nome": "Maria Oliveira",
                "email": "maria.oliveira@example.com",
                "data_nascimento": "1985-05-15",
                "senha": "senha456"
            }
        ])
        print("Coleção 'user' criada e dados iniciais inseridos.")
    else:
        print("Coleção 'user' já existe.")


# função de criação de coleções
if __name__ == "__main__":
    create_collections()

