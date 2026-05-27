from pymongo import MongoClient
from dotenv import load_dotenv

import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

# CONNECT TO MONGODB

client = MongoClient(MONGO_URI)

# DATABASE

db = client["healthcare_ai"]

# COLLECTIONS

prediction_collection = db["predictions"]

chat_collection = db["chat_history"]