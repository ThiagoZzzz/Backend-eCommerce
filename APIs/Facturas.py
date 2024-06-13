import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

class Factura:
    def __init__(self, numero_factura, cliente, fecha):
        self.numero_factura = numero_factura
        self.cliente = cliente
        self.fecha = fecha
        self.productos = []
        self.descuentos = []

    def agregar_producto(self, nombre, cantidad, precio_unitario):
        self.productos.append({
            "nombre": nombre,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "total": cantidad * precio_unitario,
            "descuento": 0
        })

    def calcular_descuento_producto(self, producto):
        descuento_total = 0
        for descuento in self.descuentos:
            if producto["nombre"] in descuento.get("productos_aplicables", []):
                descuento_total += descuento["monto"]
        return descuento_total

    def actualizar_descuentos_y_total(self):
        for producto in self.productos:
            descuento = self.calcular_descuento_producto(producto)
            producto["descuento"] = descuento
            producto["total"] = (producto["precio_unitario"] - descuento) * producto["cantidad"]

    def agregar_descuento(self, tipo, monto, productos_aplicables):
        nuevo_descuento = {
            "tipo": tipo,
            "monto": monto,
            "productos_aplicables": productos_aplicables
        }
        self.descuentos.append(nuevo_descuento)

    def calcular_total(self):
        return sum(producto['total'] for producto in self.productos)

    def to_dict(self):
        return {
            "numero_factura": self.numero_factura,
            "cliente": self.cliente,
            "fecha": self.fecha.strftime('%d/%m/%Y'),
            "productos": self.productos,
            "descuentos": self.descuentos,
            "total": self.calcular_total()
        }

@app.route('/facturacion', methods=['GET'])
def obtener_facturacion():
    factura.actualizar_descuentos_y_total()
    return jsonify(factura.to_dict())

@app.route('/facturacion/descuento', methods=['POST'])
def agregar_descuento():
    data = request.get_json()
    tipo = data.get('tipo')
    monto = data.get('monto')
    productos_aplicables = data.get('productos_aplicables')

    factura.agregar_descuento(tipo, monto, productos_aplicables)
    factura.actualizar_descuentos_y_total()

    return jsonify(factura.to_dict()), 201

if __name__ == "__main__":
    numero_factura = input("Ingrese el número de factura: ")
    cliente = input("Ingrese el nombre del cliente: ")
    fecha = datetime.datetime.now()

    factura = Factura(numero_factura, cliente, fecha)

    while True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad_producto = int(input("Ingrese la cantidad: "))
        precio_unitario_producto = float(input("Ingrese el precio unitario: "))

        factura.agregar_producto(nombre_producto, cantidad_producto, precio_unitario_producto)

        continuar = input("¿Desea agregar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break

    factura.mostrar_factura()
    app.run(debug=True)
