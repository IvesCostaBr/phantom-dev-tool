from src.infra import mongo_database


class LogRepository:
    def __init__(self):
        self.entity = "logs"
        self.db = mongo_database

    def get(self, id: str):
        """Get document."""
        return self.db.get(self.entity, id)

    def create(self, **kwargs):
        """Create document."""
        return self.db.create(self.entity, kwargs)

    def filter_query(self, **kwargs):
        """Filter documents."""
        return self.db.filter_query(self.entity, kwargs)

    def update(self, id: str, **kwargs):
        """Update document."""
        return self.db.update(self.entity, id, kwargs)

    def get_all(self):
        """Get all documents."""
        return self.db.get_all(self.entity)
