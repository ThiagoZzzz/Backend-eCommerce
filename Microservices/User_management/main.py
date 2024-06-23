from flask import Flask, request, jsonify
from flask_cors import CORS
from pyms.flask.app import Microservice

from services.config import Config
from services.db_service import DatabaseService
from services.user_service import UserService

app = Microservice(path="services")
CORS(app)

db_service = DatabaseService(Config.MONGODB_URI, Config.DB_NAME)
user_service = UserService(db_service)

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = user_service.login(username, password)
        if user:
            return jsonify({"message": "Inicio de sesión exitoso", "usuario_id": str(user['_id'])}), 200
        else:
            return jsonify({"message": "Credenciales inválidas"}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/usuarios/<usuario_id>', methods=['GET'])
def get_user(usuario_id):
    try:
        user = user_service.get_user(usuario_id)
        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')