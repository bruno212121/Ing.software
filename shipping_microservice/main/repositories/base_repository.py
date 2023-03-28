from abc import ABC, abstractmethod

class Create(ABC):
    @abstractmethod
    def create(self, objeto):
        pass

class Update(ABC):
    @abstractmethod
    def update(self, id, data):
        pass

class Delete(ABC):
    @abstractmethod
    def delete(self, id):
        pass

class Read(ABC):
    @abstractmethod
    def find_one(self, objeto):
        pass

    @abstractmethod
    def find_all(self):
        pass