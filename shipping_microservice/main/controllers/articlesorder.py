from flask_restful import Resource
from flask import request
from main.schemas import ArticlesOrderSchema
from main.services import StockService

articlesorder_schema = ArticlesOrderSchema()
stock_service = StockService()

class ArticlesOrderController(Resource):

    def post(self):
        articlesorder = articlesorder_schema.load(request.get_json())
        return articlesorder_schema.dump(stock_service.add_articlesorder(articlesorder))
    
    def get(self):
        return articlesorder_schema.dump(stock_service.get_articlesorders(), many=True)

    def put(self):
        articlesorder = articlesorder_schema.load(request.get_json())
        return articlesorder_schema.dump(stock_service.edit_articlesorder(articlesorder))
    
    def delete(self):
        articlesorder = articlesorder_schema.load(request.get_json())
        return articlesorder_schema.dump(stock_service.delete_articlesorder(articlesorder))