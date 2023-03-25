from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Article(db.Model):
    __tablename__ = 'articles'
    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String(100))
    __description = db.Column('description', db.String(100))
    __code = db.Column('code', db.Integer)
    __amount = db.Column('amount', db.Integer)
    __category_id = db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), nullable=False)
    __soft_delete = db.Column('soft_delete', db.Boolean)
    category = db.relationship('Category', back_populates='articles')

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
    def code(self):
        return self.__code
    
    @code.setter
    def code(self, code):
        self.__code = code

    @code.deleter
    def code(self):
        del self.__code
    
    @hybrid_property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @amount.deleter
    def amount(self):
        del self.__amount

    @hybrid_property
    def category_id(self):
        return self.__category_id
    
    @category_id.setter
    def category_id(self, category_id):
        self.__category_id = category_id

    @category_id.deleter
    def category_id(self):
        del self.__category_id
    
    @hybrid_property
    def soft_delete(self):
        return self.__soft_delete
    
    @soft_delete.setter
    def soft_delete(self, soft_delete):
        self.__soft_delete = soft_delete

