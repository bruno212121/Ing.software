from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Category(db.Model):

    __tablename__ = 'categories'
    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String(100))
    __description = db.Column('description', db.String(100))
    __category_code = db.Column('category_code', db.Integer)
    __soft_delete = db.Column('soft_delete', db.Boolean)
    articles = db.relationship('Article', back_populates='category', cascade="all, delete-orphan")

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
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description):
        self.__description = description

    @description.deleter
    def description(self):
        del self.__description

    @hybrid_property
    def category_code(self):
        return self.__category_code
    
    @category_code.setter
    def category_code(self, category_code):
        self.__category_code = category_code

    @category_code.deleter
    def category_code(self):
        del self.__category_code
    
    @hybrid_property
    def soft_delete(self):
        return self.__soft_delete
    
    @soft_delete.setter
    def soft_delete(self, soft_delete):
        self.__soft_delete = soft_delete

    @soft_delete.deleter
    def soft_delete(self):
        del self.__soft_delete