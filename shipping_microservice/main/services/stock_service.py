from main.schemas import ArticlesOrderSchema
from main.repositories import ArticlesOrderRepository

articlesorder_schema = ArticlesOrderSchema()
articlesorder_repository = ArticlesOrderRepository()

class StockService:

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
    