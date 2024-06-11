from flask import Blueprint, request, jsonify
from services.user_service import UserService

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Credenciales incompletas."}), 400

    user_service = UserService()
    user = user_service.authenticate(username, password)

    if user:
        return jsonify({"message": "Inicio de sesión exitoso.", "usuario_id": user['usuario_id']}), 200
    else:
        return jsonify({"message": "Credenciales inválidas."}), 401