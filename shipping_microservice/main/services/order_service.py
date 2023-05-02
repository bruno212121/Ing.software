from main.schemas import ArticlesOrderSchema, OrderSchema
from main.repositories import ArticlesOrderRepository, OrderRepository
import requests, os
from main import db_breaker

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
    def get_articles_order(self, id):
        return articlesorder_repository.find_all_by_id(id)
    
    @db_breaker
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
    def get_order(self, id):
        return order_repository.find_by_id(id)
    
    @db_breaker
    def get_orders(self):
        return order_repository.find_all()
    
    @db_breaker
    def get_articles(self):
        print(os.getenv("ARTICLES_API"), 'URL API')
        articles = requests.get(f'{os.getenv("ARTICLES_API")}/articles', headers={'Content-Type': 'application/json'})
        return articles.json()
    