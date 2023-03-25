from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
import os

class ArticlesOrder(db.Model):
    __tablename__ = 'articles_orders'
    __id = db.Column('id', db.Integer, primary_key=True)
    __order_id = db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable=False)
    # __article_id = db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    __article_id = db.Column('article_id', db.Integer, nullable=False)              # TODO: como no puedo hacer que sea FK porque article no exsite en este microservicio es decir esta en otro, solo guardo el id del articulo por ahora...
    __ammount_article = db.Column('ammount_article', db.Integer, nullable=False)
    __soft_delete = db.Column('soft_delete', db.Boolean, default=False)

    # TODO: esto supuestamente lo arreglaba, pero no anduvo nada :(
    # __table_args__ = {'schema': f'{os.getenv("DB_DATABASE")}'}
    # articles = db.Table('articles',
    # db.Column('id', db.Integer),
    # db.Column('name', db.String(100)),
    # db.Column('description', db.String(100)),
    # db.Column('code', db.Integer),
    # db.Column('amount', db.Integer),
    # db.Column('category_id', db.Integer),
    # db.Column('soft_delete', db.Boolean),
    # )

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
    def order_id(self):
        return self.__order_id
    
    @order_id.setter
    def order_id(self, order_id):
        self.__order_id = order_id

    @order_id.deleter
    def order_id(self):
        del self.__order_id

    @hybrid_property
    def article_id(self):
        return self.__article_id
    
    @article_id.setter
    def article_id(self, article_id):
        self.__article_id = article_id

    @article_id.deleter
    def article_id(self):
        del self.__article_id

    @hybrid_property
    def ammount_article(self):
        return self.__ammount_article
    
    @ammount_article.setter
    def ammount_article(self, ammount_article):
        self.__ammount_article = ammount_article

    @ammount_article.deleter
    def ammount_article(self):
        del self.__ammount_article

    @hybrid_property
    def soft_delete(self):
        return self.__soft_delete
    
    @soft_delete.setter
    def soft_delete(self, soft_delete):
        self.__soft_delete = soft_delete

    @soft_delete.deleter
    def soft_delete(self):
        del self.__soft_delete