from pymongo.mongo_client import MongoClient
from bson import ObjectId
from src.infra.cache import cache_manager
from datetime import datetime
import time


class MongoDatabase:
    def __init__(self, connection_string: str, port: int, db_name):
        """Initialize class with connection string and database name."""
        self.host = connection_string
        self.port = int(port)
        self.db_name = db_name
        self.db = None
        self.client = None

        self.create_connection()

    def create_connection(self):
        """Create connection with MongoDB."""
        try:
            self.client = MongoClient(self.host, self.port)
            print("MongoDB connected successfully!!")
            self.db = self.client[self.db_name]
        except Exception as ex:
            raise Exception(f"error connect database {str(ex)}")

    def get(self, entity: str, id: str, use_cache: bool = True):
        value_cached = cache_manager.get(id) if use_cache else False
        if not value_cached:
            try:
                object_id = ObjectId(id)
            except:
                object_id = id
            doc = self.db[entity].find_one({"_id": object_id})
            if doc is not None:
                doc["id"] = str(doc["_id"])
                doc.pop("_id")
                cache_manager.save(id, doc, 1200)
                return doc
            else:
                return None
        else:
            return value_cached

    def get_all(self, entity: str, limit: int = 100):
        docs = list(self.db[entity].find().limit(limit))
        for each in docs:
            each["id"] = str(each.get("_id"))
            each.pop("_id")
        return docs

    def __format_filter(self, query: dict) -> list:
        filter_formated = []
        for key, value in query.items():
            if "__" not in key.lower():
                filter_formated.append({key: value})
            elif "__lt" in key.lower():
                filter_formated.append(
                    {key.replace("__lt", ""): {"$lt": value}})
            elif "__lte" in key.lower():
                filter_formated.append(
                    {key.replace("__lte", ""): {"$lte": value}})
            elif "__range" in key.lower():
                start, end = value
                filter_formated.append(
                    {key.replace("__range", ""): {"$gte": start, "$lte": end}}
                )
            elif "__gt" in key.lower():
                filter_formated.append(
                    {key.replace("__gt", ""): {"$gt": value}})
            elif "__gte" in key.lower():
                filter_formated.append(
                    {key.replace("__gte", ""): {"$gte": value}})
            elif "__in" in key.lower():
                filter_formated.append(
                    {key.replace("__in", ""): {"$in": value}})
            elif "__in" in key.lower():
                filter_formated.append(
                    {key.replace("__nt", ""): {"$not": value}})
        return filter_formated

    def create(self, entity: str, data: dict, id: str = None):
        data["created_at"] = time.mktime(datetime.now().timetuple())
        if id:
            data["_id"] = id
        new_data = self.db[entity].insert_one(data)
        return str(new_data.inserted_id)

    def update(self, entity: str, id: str, data: dict):
        try:
            if "id" in data.keys():
                data.pop("id")
            id = ObjectId(id)
        except:
            None
        data["updated_at"] = time.mktime(datetime.now().timetuple())
        update_operation = {"$set": data}
        try:
            self.db[entity].update_one(
                {"_id": id}, update_operation, upsert=False)
            return True
        except:
            return False

    def filter_query(self, entity: str, query: dict, exclude_fields: list = []):
        response_list = []
        formatted_query = self.__format_filter(query)
        result = self.db[entity].find({"$and": formatted_query})
        if not result:
            return []
        for each in result:
            each["id"] = str(each["_id"])
            each.pop("_id")
            if exclude_fields:
                each = {
                    key: value
                    for key, value in each.items()
                    if key not in exclude_fields
                }
            response_list.append(each)
        return response_list

    def exists(self, entity: str, query: dict):
        result = self.db[entity].find(query)
        return list(result)

    def delete(self, entity: str, id: str):
        """Delete document."""
        try:
            id = ObjectId(id)
        except:
            None
        try:
            self.db[entity].delete_one({"_id": id})
            return True
        except:
            return False
