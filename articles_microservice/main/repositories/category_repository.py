from .. import db
from .base_repository import Create, Update, Delete, Read
from main.models import CategoryModel

class CategoryRepository(Create, Update, Delete, Read):

    def __init__(self):
        self.model = CategoryModel

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def update(self, id, data):
        objeto = self.model.query.get(id)
        for key, value in data.items():
            setattr(objeto, key, value)
        db.session.commit()
        return objeto

    def delete(self, id):
        objeto = self.model.query.get(id)
        db.session.delete(objeto)
        db.session.commit()
        return objeto

    def find_one(self, objeto):
        return self.model.query.filter_by(**objeto).first()

    def find_all(self):
        return self.model.query.all()
    
    def find_by_id(self, id):
        return db.session.query(self.model).get(id)