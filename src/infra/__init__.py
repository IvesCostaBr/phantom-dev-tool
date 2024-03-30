
from src.infra.database.mongo_connection import MongoDatabase
import os


mongo_database = MongoDatabase(
    os.environ.get("MONGO_HOST"),
    os.environ.get("MONGO_PORT"),
    "phantom",
)
