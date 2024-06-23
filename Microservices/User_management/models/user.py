from pymongo import MongoClient
from bson.objectid import ObjectId

class User:
    def __init__(self, db):
        self.collection = db['users']
    
    def find_user_by_username(self, username):
        return self.collection.find_one({"username": username})
    
    def validate_user(self, username, password):
        user = self.find_user_by_username(username)
        if user and user['password'] == password:
            return user
        return None
    
    def get_user_by_id(self, user_id):
        return self.collection.find_one({"_id": ObjectId(user_id)})