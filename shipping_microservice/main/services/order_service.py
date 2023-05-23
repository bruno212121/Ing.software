from main.schemas import ArticlesOrderSchema, OrderSchema
from main.repositories import ArticlesOrderRepository, OrderRepository
import requests, os
from flask_cors import cross_origin
from flask import Blueprint, request
import random, time
from main import cache
from main import db_breaker

order_api = Blueprint('order_api', __name__)

articlesorder_schema = ArticlesOrderSchema()
articlesorder_repository = ArticlesOrderRepository()
order_repository = OrderRepository()
order_schema = OrderSchema()

class OrderService:

    #articlesorder
    @db_breaker
    def add_article_order(self, articlesorder):
        articlesorder_repository.create(articlesorder)
        return articlesorder_schema.dump(articlesorder)
    
    # def get_articles_orders(self):
    #     return articlesorder_repository.find_all()

    @db_breaker
    @cache.cached(timeout=500)
    def get_articles_order(self, id):
        return articlesorder_repository.find_all_by_id(id)
    
    @db_breaker
    @cache.cached(timeout=500)
    def get_article_order(self, id):
        return articlesorder_repository.find_by_id(id)
    
    @db_breaker
    def edit_articlesorder(self, articlesorder):
        articlesorder_repository.update(articlesorder)
        return articlesorder_schema.dump(articlesorder)
    
    @db_breaker
    def delete_articlesorder(self, articlesorder):
        articlesorder_repository.delete(articlesorder)
        return articlesorder_schema.dump(articlesorder)
    
    @db_breaker
    def add_order(self, order):
        order_repository.create(order)
        return order_schema.dump(order)
    
    @db_breaker
    @cache.cached(timeout=500)
    def get_order(self, id):
        return order_repository.find_by_id(id)
    
    @db_breaker
    @cache.cached(timeout=500)
    def get_orders(self):
        return order_repository.find_all()
    
    @db_breaker
    @cache.cached(timeout=500)
    def get_articles(self):
        print(os.getenv("ARTICLE_API"), 'URL API')
        try:
            articles = requests.get(f'{os.getenv("ARTICLE_API")}/articles', headers={'Content-Type': 'application/json'}, verify=False)
        except Exception as e:
            print(e)
            articles = {'error': 'No se pudo conectar con el servicio de articulos'}
            return articles
        return articles.json()
    
@order_api.route('/articulos', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_articles():
    headers = {'Origin': 'http://shipping.order.localhost'}
    response = requests.get('http://article.order.localhost/articles', headers=headers)
    return response.json()

@db_breaker
@order_api.route('/proof', methods=['GET'])
def proof():
    # codigo = request.get_json()['codigo']

    seed = random.randint(1, 100)
    codigos = [404, 500, "latencia"]
    # codigo = random.choice(codigos)
    codigo = codigos[seed % 3]
    if codigo == 404:
        return "No se encontró el recurso", 404
    elif codigo == 500:
        return "Error interno del servidor", 500
    elif codigo == "latencia":
        time.sleep(10)
        return "Error latencia del servidor", 500