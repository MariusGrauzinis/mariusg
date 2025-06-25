def analyze_prompt(prompt):
    # čia tavo analizės logika (arba burbulas iki MongoDB fazės)
    return f"Analizuotas prompt: {prompt}"

from flask import current_app
from pymongo import MongoClient
import os

def get_db():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/promptanalyzer")
    client = MongoClient(mongo_uri)
    db = client.get_database()
    return db
