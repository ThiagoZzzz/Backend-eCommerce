from flask import Flask, request, jsonify
from flask_cors import CORS
from pyms.flask.app import Microservice
import stripe

from services.config import Config
from services.db_service import DatabaseService
from services.pedido_service import PedidoService

app = Microservice(path="services")
CORS(app)

db_service = DatabaseService(Config.MONGODB_URI, Config.DB_NAME)
pedido_service = PedidoService(db_service)

stripe.api_key = Config.STRIPE_SECRET_KEY

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        data = request.get_json()
        items = data.get('items', [])

        if not items:
            return jsonify({'error': 'No items provided'}), 400

        line_items = [{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item['title'],
                },
                'unit_amount': int(item['price']),
            },
            'quantity': item['quantity'],
        } for item in items]

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url='https://ecommerce-oficial.vercel.app/',
            cancel_url='https://ecommerce-oficial.vercel.app/',
        )
        return jsonify({'sessionId': session.id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pedidos/<usuario_id>', methods=['GET'])
def get_pedidos(usuario_id):
    try:
        pedidos = pedido_service.get_pedidos(usuario_id)
        return jsonify(pedidos), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pedidos/<usuario_id>', methods=['POST'])
def add_pedido(usuario_id):
    try:
        pedido = request.get_json()
        pedido_service.add_pedido(usuario_id, pedido)
        return jsonify({'message': 'Pedido added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=4242, host='0.0.0.0')