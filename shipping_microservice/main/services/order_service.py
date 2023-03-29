from main.schemas import ArticlesOrderSchema, OrderSchema
from main.repositories import ArticlesOrderRepository, OrderRepository

articlesorder_schema = ArticlesOrderSchema()
articlesorder_repository = ArticlesOrderRepository()
order_repository = OrderRepository()
order_schema = OrderSchema()

class OrderService:

    #articlesorder
    def add_articlesorder(self, articlesorder):
        articlesorder_repository.create(articlesorder)
        return articlesorder_schema.dump(articlesorder)
    
    def get_articlesorders(self):
        return articlesorder_repository.find_all()
    
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
    