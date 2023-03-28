from flask_restful import Resource
from flask import request
from main.schemas import ArticleSchema
from main.services import StockService

article_schema = ArticleSchema()
stock_service = StockService()

class ArticleController(Resource):

    def post(self):
        article = article_schema.load(request.get_json())
        return article_schema.dump(stock_service.add_article(article))
    
    def get(self):
        return article_schema.dump(stock_service.get_articles(), many=True)

    def put(self):
        article = article_schema.load(request.get_json())
        return article_schema.dump(stock_service.edit_article(article))
    
    def delete(self):
        article = article_schema.load(request.get_json())
        return article_schema.dump(stock_service.delete_article(article))