from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    __id = db.Column('id', db.Integer, primary_key=True)
    __order_code = db.Column('order_code', db.String(100), nullable=False)
    __date = db.Column('date', db.DateTime, default=datetime.datetime.now())
    __sucursal_id = db.Column('sucursal_id', db.Integer, db.ForeignKey('sucursales.id'), nullable=False)
    __status_out = db.Column('status_out', db.Boolean, default=False)
    __soft_delete = db.Column('soft_delete', db.Boolean, default=False)
    sucursal = db.relationship('Sucursal', back_populates='orders')

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
    def order_code(self):
        return self.__order_code
    
    @order_code.setter
    def order_code(self, order_code):
        self.__order_code = order_code

    @order_code.deleter
    def order_code(self):
        del self.__order_code

    @hybrid_property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date

    @date.deleter
    def date(self):
        del self.__date

    @hybrid_property
    def sucursal_id(self):
        return self.__sucursal_id
    
    @sucursal_id.setter
    def sucursal_id(self, sucursal_id):
        self.__sucursal_id = sucursal_id

    @sucursal_id.deleter
    def sucursal_id(self):
        del self.__sucursal_id

    @hybrid_property
    def status_out(self):
        return self.__status_out
    
    @status_out.setter
    def status_out(self, status_out):
        self.__status_out = status_out

    @status_out.deleter
    def status_out(self):
        del self.__status_out

    @hybrid_property
    def soft_delete(self):
        return self.__soft_delete
    
    @soft_delete.setter
    def soft_delete(self, soft_delete):
        self.__soft_delete = soft_delete

    @soft_delete.deleter
    def soft_delete(self):
        del self.__soft_delete

