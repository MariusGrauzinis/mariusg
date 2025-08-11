import random
from datetime import datetime, timedelta
from pymongo import MongoClient
from typing import List

# Sources of random data generation
NAMES = ["Jonas", "Mantas", "Ieva", "Antanas", "Lina", "Tomas", "Laura", "Dovile", "Justas", "Rugile", "Andrius"]
TITLES = [
    "First post", 
    "Simple example", 
    "Learning Python", 
    "Working with MongoDB", 
    "Random data test", 
    "Intro to databases", 
    "My second article", 
    "Database project", 
    "Data entry test", 
    "Mongo CRUD demo"
]
TAGS = ["MongoDB", "Python", "CRUD", "Tutorial", "Dev", "Spreadsheet", "Document"]

# Update for random data
NAMES += ["Egle", "Karolis", "Vaida", "Simas", "Rasa", "Emilija", "Paulius", "Greta", "Dominykas", "Vilte"]
TITLES += [
    "Exploring NoSQL Concepts",
    "Python vs JavaScript",
    "Top 5 MongoDB Tips",
    "Handling JSON in Databases",
    "Getting Started with APIs",
    "My Coding Journey",
    "Understanding Indexes",
    "Fast Queries with MongoDB",
    "Simple Logging with Python",
    "Writing Cleaner Code"
]
TAGS += ["Indexing", "Performance", "Best Practices", "NoSQL", "REST", "Backend", "Testing", "Data Science", "CLI", "Security"]

# Remove duplicates but keep order (optional)
NAMES = list(dict.fromkeys(NAMES))
TITLES = list(dict.fromkeys(TITLES))
TAGS = list(dict.fromkeys(TAGS))

# Creating new document
def generate_random_document() -> dict:
    name = random.choice(NAMES)
    title = random.choice(TITLES)
    created_at = datetime.now() - timedelta(days=random.randint(0, 365))
    updated_at = created_at + timedelta(hours=random.randint(1, 72))

    return {
        "title": title,
        "content": f"This is randomly generated article about {title}.",
        "author": {
            "name": name,
            "email": f"{name.lower()}@example.com"
        },
        "tags": random.sample(TAGS, k=random.randint(1, 3)),
        "createdAt": created_at,
        "updatedAt": updated_at
    }

# Save to MongoDB
def insert_random_documents(n: int, db_name: str, collection_name: str):
    client = MongoClient("localhost", 27017)
    db = client[db_name]
    collection = db[collection_name]

    documents: List[dict] = [generate_random_document() for _ in range(n)]
    result = collection.insert_many(documents)

    print(f"Inserted {len(result.inserted_ids)} documents into '{collection_name}' collection.")

def print_all_documents(db_name: str, collection_name: str):
    client = MongoClient("localhost", 27017)
    db = client[db_name]
    collection = db[collection_name]

    print(f"\nDocuments in '{collection_name}' collection:")
    for post in collection.find():
        print(post)

if __name__ == "__main__":
    number_of_documents = 15  # Keisk jei nori daugiau ar mažiau
    insert_random_documents(number_of_documents, "blogDB", "posts")
    print_all_documents("blogDB", "posts")
