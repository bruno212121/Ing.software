from .. import db
from .base_repository import Create, Update, Delete, Read
from main.models import SucursalModel

class SucursalRepository(Create):

    def __init__(self):
        self.model = SucursalModel

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto
    
    def find_by_id(self, id):
        return db.session.query(self.model).get(id)
    

