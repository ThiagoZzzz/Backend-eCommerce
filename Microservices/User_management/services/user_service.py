from models.user import User

class UserService:
    def __init__(self, db_service):
        self.user_model = User(db_service.get_db())
    
    def login(self, username, password):
        user = self.user_model.validate_user(username, password)
        if user:
            return user
        return None
    
    def get_user(self, user_id):
        return self.user_model.get_user_by_id(user_id)