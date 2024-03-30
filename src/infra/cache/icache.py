from abc import ABC, abstractmethod


class ICacheCliente(ABC):
    @abstractmethod
    def create(self, key: str, value: object, ttl: int):
        """abstract method for create data in cache."""
        raise NotImplementedError()

    @abstractmethod
    def get(self, key: str):
        """abstract method for get data in cache."""
        raise NotImplementedError()

    @abstractmethod
    def remove(self, key: str):
        """abstract method remove data in cache."""
        raise NotImplementedError()
