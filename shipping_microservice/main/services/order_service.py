from main.schemas import ArticlesOrderSchema, OrderSchema
from main.repositories import ArticlesOrderRepository, OrderRepository
import requests, os
from flask_cors import cross_origin
from flask import Blueprint, request
import random, time

order_api = Blueprint('order_api', __name__)

articlesorder_schema = ArticlesOrderSchema()
articlesorder_repository = ArticlesOrderRepository()
order_repository = OrderRepository()
order_schema = OrderSchema()

class OrderService:

    #articlesorder
    def add_article_order(self, articlesorder):
        articlesorder_repository.create(articlesorder)
        return articlesorder_schema.dump(articlesorder)
    
    # def get_articles_orders(self):
    #     return articlesorder_repository.find_all()

    def get_articles_order(self, id):
        return articlesorder_repository.find_all_by_id(id)
    
    def get_article_order(self, id):
        return articlesorder_repository.find_by_id(id)
    
    def edit_articlesorder(self, articlesorder):
        articlesorder_repository.update(articlesorder)
        return articlesorder_schema.dump(articlesorder)
    
    def delete_articlesorder(self, articlesorder):
        articlesorder_repository.delete(articlesorder)
        return articlesorder_schema.dump(articlesorder)
    
    def add_order(self, order):
        order_repository.create(order)
        return order_schema.dump(order)
    
    def get_order(self, id):
        return order_repository.find_by_id(id)
    
    def get_orders(self):
        return order_repository.find_all()
    
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

@order_api.route('/proof', methods=['GET'])
def proof():
    # codigo = request.get_json()['codigo']
    codigos = [404, 500, "latencia"]
    codigo = random.choice(codigos)
    if codigo == 404:
        return "No se encontró el recurso", 404
    elif codigo == 500:
        return "Error interno del servidor", 500
    elif codigo == "latencia":
        time.sleep(10)
        return "Error latencia del servidor", 500