from flask_restful import Resource
from flask import request
from main.schemas import ArticleSchema
from main.services import StockService
from main import cache

article_schema = ArticleSchema()
stock_service = StockService()

class ArticlesController(Resource):


    def post(self):
        article = article_schema.load(request.get_json())
        return article_schema.dump(stock_service.add_article(article))
    
    @cache.cached(timeout=50)
    def get(self):
        return article_schema.dump(stock_service.get_articles(), many=True)
    
    def put(self):
        article = article_schema.load(request.get_json())
        return article_schema.dump(stock_service.edit_article(article))
    
class ArticleController(Resource):

    def delete(self, id):
        article = stock_service.get_article(id)
        return article_schema.dump(stock_service.soft_delete_article(article))