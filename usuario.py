from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM usuarios'
        results = connectToMySQL('usuarios').query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append( cls(usuario))
        return usuarios

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (first_name, last_name, email, created_at, updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s, NOW() , NOW() ); "
        return connectToMySQL('usuarios').query_db(query , data)

