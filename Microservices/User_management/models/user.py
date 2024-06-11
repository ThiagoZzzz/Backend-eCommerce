class User:
    def __init__(self, username, password, usuario_id, email, nombre):
        self.username = username
        self.password = password
        self.usuario_id = usuario_id
        self.email = email
        self.nombre = nombre

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "username": self.username,
            "email": self.email,
            "nombre": self.nombre
        }