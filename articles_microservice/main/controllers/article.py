from flask_restful import Resource
from flask import request, jsonify
from main.schemas import ArticleSchema
from main.services import StockService
from main import cache
import pybreaker


article_schema = ArticleSchema()
stock_service = StockService()

class ArticlesController(Resource):


    def post(self):
        try:
            article = article_schema.load(request.get_json())
            return article_schema.dump(stock_service.add_article(article))
        except pybreaker.CircuitBreakerError as e:
            print(f"CircuitBreakerError: {e}")
            #return jsonify({"error": "Circuit breaker is open"}), 500
            #preguntar al profe problema con el jsonify
            
    @cache.cached(timeout=50)
    def get(self):
        try:
            #stock_service.faulty_method()
            return article_schema.dump(stock_service.get_articles(), many=True)
        except pybreaker.CircuitBreakerError as e:
            print(f"CircuitBreakerError: {e}")
            #return jsonify({"error": "Circuit breaker is open"}), 500
            #preguntar al profe problema con el jsonify

    def put(self):
        try:
            article = article_schema.load(request.get_json())
            return article_schema.dump(stock_service.edit_article(article))
        except pybreaker.CircuitBreakerError as e:
            print(f"CircuitBreakerError: {e}")
            #return jsonify({"error": "Circuit breaker is open"}), 500
            #preguntar al profe problema con el jsonify

class ArticleController(Resource):

    def delete(self, id):
        try:
            article = stock_service.get_article(id)
            return article_schema.dump(stock_service.soft_delete_article(article))
        except pybreaker.CircuitBreakerError as e:
            print(f"CircuitBreakerError: {e}")
            #return jsonify({"error": "Circuit breaker is open"}), 500
            #preguntar al profe problema con el jsonify