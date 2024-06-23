class Pedido:
    def __init__(self, pedido_id, estado, productos):
        self.pedido_id = pedido_id
        self.estado = estado
        self.productos = productos

    def to_dict(self):
        return {
            "pedido_id": self.pedido_id,
            "estado": self.estado,
            "productos": self.productos
        }