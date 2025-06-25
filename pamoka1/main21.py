from datetime import datetime

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


documents_list = [
    {
        "title": "Introduction to Python",
        "content": "Python is a versatile programming language that's great for beginners and experts alike...",
        "author": {"name": "John Smith", "email": "johnsmith@example.com"},
        "tags": ["Python", "Programming", "Beginner"],
        "createdAt": datetime(2024, 1, 10, 9, 30, 0),
        "updatedAt": datetime(2024, 1, 11, 16, 45, 0),
    },
    {
        "title": "Advanced MongoDB Queries",
        "content": "Learn how to write complex queries in MongoDB using various operators and techniques...",
        "author": {"name": "Sarah Wilson", "email": "sarahwilson@example.com"},
        "tags": ["MongoDB", "Database", "Queries", "Advanced"],
        "createdAt": datetime(2024, 2, 5, 14, 20, 0),
        "updatedAt": datetime(2024, 2, 6, 10, 15, 0),
    },
    {
        "title": "Web Development with Flask",
        "content": "Flask is a lightweight web framework for Python that makes building web applications easy...",
        "author": {"name": "Mike Davis", "email": "mikedavis@example.com"},
        "tags": ["Flask", "Web Development", "Python", "Framework"],
        "createdAt": datetime(2024, 3, 12, 11, 0, 0),
        "updatedAt": datetime(2024, 3, 13, 9, 30, 0),
    },
    {
        "title": "Data Analysis with Pandas",
        "content": "Pandas is a powerful data manipulation library that simplifies data analysis tasks...",
        "author": {"name": "Emily Chen", "email": "emilychen@example.com"},
        "tags": ["Pandas", "Data Analysis", "Python", "Data Science"],
        "createdAt": datetime(2024, 4, 8, 13, 15, 0),
        "updatedAt": datetime(2024, 4, 9, 15, 22, 0),
    },
    {
        "title": "Machine Learning Fundamentals",
        "content": "An introduction to machine learning concepts and algorithms for beginners...",
        "author": {"name": "Robert Taylor", "email": "roberttaylor@example.com"},
        "tags": ["Machine Learning", "AI", "Algorithms", "Data Science"],
        "createdAt": datetime(2024, 5, 20, 16, 40, 0),
        "updatedAt": datetime(2024, 5, 21, 12, 10, 0),
    },
]


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def insert_document(collection: Collection, document: dict) -> str:
    result = collection.insert_one(document)
    return str(result.inserted_id)


def insert_many_documents(collection: Collection, documents: list[dict]) -> list[str]:
    result = collection.insert_many(documents)
    return [str(id) for id in result.inserted_ids]


# Example usage
if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "blogDB"
    collection_name = "posts"

    try:
        # Connect to MongoDB
        db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

        # Retrieve a specific collection
        collection = db[collection_name]

        # # Create (Insert) Operation
        # document = {
        #     "title": "Understanding MongoDB Aggregation",
        #     "content": "Aggregation in MongoDB allows you to process and transform data "
        #     "effectively...",
        #     "author": {"name": "Alice Johnson", "email": "alicejohnson@example.com"},
        #     "tags": ["MongoDB", "Aggregation", "Data Processing"],
        #     "createdAt": datetime(2024, 10, 15, 8, 45, 0),
        #     "updatedAt": datetime(2024, 10, 16, 14, 20, 0),
        # }
        # inserted_id = insert_document(collection, document)
        result = insert_many_documents(collection, documents_list)
        print(f"Inserted document with ID: {result}")
    except Exception as e:
        print(f"Error occurred: {e}")
   