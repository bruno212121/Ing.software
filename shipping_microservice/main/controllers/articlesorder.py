from flask_restful import Resource
from flask import request
from flask import jsonify
from main.schemas import ArticlesOrderSchema
from main.services import OrderService
import pybreaker

articlesorder_schema = ArticlesOrderSchema()
order_service = OrderService()

class ArticlesOrderController(Resource):

    def post(self):
        try:
            article_order = articlesorder_schema.load(request.get_json())
            return articlesorder_schema.dump(order_service.add_article_order(article_order))
        except pybreaker.CircuitBreakerError as e:
            print(f"CircuitBreakerError: {e}")
            #return jsonify({"error": "Circuit breaker is open"}), 500
            #preguntar al profe problema con el jsonify
        
    def get(self): ...
        # return articlesorder_schema.dump(stock_service.get_articlesorders(), many=True)

    def put(self):
        try:
            articles_order = articlesorder_schema.load(request.get_json())
            # return articlesorder_schema.dump(stock_service.edit_articlesorder(articlesorder))
        except pybreaker.CircuitBreakerError as e:
            print(f"CircuitBreakerError: {e}")
            #return jsonify({"error": "Circuit breaker is open"}), 500
            #preguntar al profe problema con el jsonify
        
    def delete(self):
        try:
            articles_order = articlesorder_schema.load(request.get_json())
            # return articlesorder_schema.dump(stock_service.delete_articlesorder(articlesorder))
        except pybreaker.CircuitBreakerError as e:
            print(f"CircuitBreakerError: {e}")
            #return jsonify({"error": "Circuit breaker is open"}), 500
            #preguntar al profe problema con el jsonify