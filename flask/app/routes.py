from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017")  # "mongo" – tai konteinerio vardas
db = client.testdb

@app.route('/')
def home():
    return 'API veikia!'

@app.route('/mongo-test')
def mongo_test():
    db.test.insert_one({"zinute": "veikia!"})
    count = db.test.count_documents({})
    return f"MongoDB yra {count} dokumentų."