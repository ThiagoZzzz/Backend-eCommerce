from models.user import User

class UserService:

    def __init__(self):
        # Conexión a la base de datos de los usuarios (creada en MongoDB)
        self.users = {
            "123456": User("usuario1", "password123", "123456", "usuario1@example.com", "Usuario Uno")
        }

    def authenticate(self, username, password):
        for user in self.users.values():
            if user.username == username and user.password == password:
                return user.to_dict()
        return None

    def get_user_by_id(self, usuario_id):
        user = self.users.get(usuario_id)
        if user:
            return user.to_dict()
        return None
