from flask import Flask, request, jsonify
from flask_cors import CORS
import stripe

app = Flask(__name__)
CORS(app)
stripe.api_key = 'sk_test_51POO55HPStxLJRgyaXaciMybVn5j1fWM8Cwq2VDhG7VCw0rhntnfowePjfJ7M3BxKnvU09QWFgq0r9BrB6CA2MJ600P5HEvM9q'  # Reemplaza con tu Secret Key de Stripe

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        data = request.get_json()
        items = data.get('items', [])

        if not items:
            return jsonify({'error': 'No items provided'}), 400

        line_items = [{
            'price_data': {
                'currency': 'ars',
                'product_data': {
                    'name': item['title'],
                },
                'unit_amount': int(item['price']),  # Se espera que el precio ya esté en centavos
            },
            'quantity': item['quantity'],
        } for item in items]

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url='http://127.0.0.1:5501/success.html',
            cancel_url='http://127.0.0.1:5501/cancel.html',
        )
        return jsonify({'sessionId': session.id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=4242, host='0.0.0.0')
