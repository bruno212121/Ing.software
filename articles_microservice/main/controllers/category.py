from flask_restful import Resource
from flask import request, jsonify
from main.schemas import CategorySchema
from main.services import StockService
import pybreaker

category_schema = CategorySchema()
stock_service = StockService()

class CategoryController(Resource):
    
    def post(self):
        try:
            category = category_schema.load(request.get_json())
            return category_schema.dump(stock_service.add_category(category))
        except pybreaker.CircuitBreakerError as e:
            print(f"CircuitBreakerError: {e}")
            #return jsonify({"error": "Circuit breaker is open"}), 500
            #preguntar al profe problema con el jsonify