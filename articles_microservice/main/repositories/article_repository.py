from .. import db
from .base_repository import Create, Update, Delete, Read
from main.models import ArticleModel

class ArticleRepository(Create, Update, Delete, Read):

    def __init__(self):
        self.model = ArticleModel

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def update(self, data):
        db.session.add(data)
        db.session.commit()
        return data

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
    
    def soft_delete(self, objeto):
        objeto.soft_delete = True
        return self.update(objeto)