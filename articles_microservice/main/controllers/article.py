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
