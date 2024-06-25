from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MONGODB_URI = os.getenv("MONGODB_URI")
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
    DB_NAME = os.getenv("DB_NAME")