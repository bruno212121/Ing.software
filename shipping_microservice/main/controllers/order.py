from flask_restful import Resource
from flask import request
from flask import jsonify
from main.schemas import OrderSchema
from main.services import OrderService
from main import cache
import pybreaker

order_schema = OrderSchema()
order_service = OrderService() 

class OrderController(Resource):

    def post(self):
        try:
            order = order_schema.load(request.get_json())
            return order_schema.dump(order_service.add_order(order))
        except pybreaker.CircuitBreakerError as e:
            return jsonify({"error": "Circuit breaker is open"}), 500
        
    @cache.cached(timeout=500000)
    def get(self):
        try:
            return order_schema.dump(order_service.get_orders(), many=True)
        except pybreaker.CircuitBreakerError as e:
            return jsonify({"error": "Circuit breaker is open"}), 500
        
class ArticlesController(Resource):

    def get(self):
        try:
            return order_service.get_articles()
        except pybreaker.CircuitBreakerError as e:
            return jsonify({"error": "Circuit breaker is open"}), 500