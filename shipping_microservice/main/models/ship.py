from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Ship(db.Model):
    __tablename__ = 'ships'
    __id = db.Column('id', db.Integer, primary_key=True)
    __id_order = db.Column('id_order', db.Integer, db.ForeignKey('orders.id'), nullable=False)
    __ship_code = db.Column('ship_code', db.String(100))
    __status = db.Column('status', db.String(100), default='pending')
    __soft_delete = db.Column('soft_delete', db.Boolean, default=False)
    # order = db.relationship('Order', back_populates='ships')

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
    def id_order(self):
        return self.__id_order
    
    @id_order.setter
    def id_order(self, id_order):
        self.__id_order = id_order

    @id_order.deleter
    def id_order(self):
        del self.__id_order

    @hybrid_property
    def ship_code(self):
        return self.__ship_code
    
    @ship_code.setter
    def ship_code(self, ship_code):
        self.__ship_code = ship_code

    @ship_code.deleter
    def ship_code(self):
        del self.__ship_code

    @hybrid_property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

    @status.deleter
    def status(self):
        del self.__status

    @hybrid_property
    def soft_delete(self):
        return self.__soft_delete
    
    @soft_delete.setter
    def soft_delete(self, soft_delete):
        self.__soft_delete = soft_delete

    @soft_delete.deleter
    def soft_delete(self):
        del self.__soft_delete
