from flask_restful import Resource
from flask import request
from main.schemas import CategorySchema
from main.services import StockService

category_schema = CategorySchema()
stock_service = StockService()

class CategoryController(Resource):
    
        def post(self):
            category = category_schema.load(request.get_json())
            return category_schema.dump(stock_service.add_category(category))