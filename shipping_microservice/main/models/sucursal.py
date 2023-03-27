from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Sucursal(db.Model):
    __tablename__ = 'sucursales'
    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String(100))
    __admin = db.Column('admin', db.Boolean)
    __soft_delete = db.Column('soft_delete', db.Boolean)
    orders = db.relationship('Order', back_populates='sucursal')

    @hybrid_property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
        
    @id.deleter
    def id(self):
        del self.__id

    @hybrid_property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @hybrid_property
    def admin(self):
        return self.__admin
    
    @admin.setter
    def admin(self, admin):
        self.__admin = admin

    @admin.deleter
    def admin(self):
        del self.__admin

    @hybrid_property
    def soft_delete(self):
        return self.__soft_delete
    
    @soft_delete.setter
    def soft_delete(self, soft_delete):
        self.__soft_delete = soft_delete

    @soft_delete.deleter
    def soft_delete(self):
        del self.__soft_delete
        