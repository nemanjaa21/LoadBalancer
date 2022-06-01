from abc import ABC, abstractmethod


class CRUD(ABC):

    @abstractmethod
    def read(self, *args):
        pass

    @abstractmethod
    def insert(self, *args):
        pass

    @abstractmethod
    def delete(self, *args):
        pass

    @abstractmethod
    def update(self, *args):
        pass
