class PedidoService:
    def __init__(self, db_service):
        self.users_collection = db_service.get_collection('users')
    
    def get_pedidos(self, usuario_id):
        user = self.users_collection.find_one({"_id": usuario_id})
        if user:
            return user.get('historial_pedidos', [])
        return []

    def add_pedido(self, usuario_id, pedido):
        self.users_collection.update_one(
            {"_id": usuario_id},
            {"$push": {"historial_pedidos": pedido}}
        )