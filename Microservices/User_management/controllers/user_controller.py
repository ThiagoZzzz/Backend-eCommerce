from flask import Blueprint, jsonify
from services.user_service import UserService

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/api/usuarios/<usuario_id>', methods=['GET'])
def get_user(usuario_id):
    user_service = UserService()
    user = user_service.get_user_by_id(usuario_id)

    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "Usuario no encontrado."}), 404