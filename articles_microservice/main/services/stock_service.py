from main.schemas import ArticleSchema, CategorySchema
from main.repositories import ArticleRepository, CategoryRepository
from main import db_breaker

article_schema = ArticleSchema()
article_repository = ArticleRepository()
category_schema = CategorySchema()
category_repository = CategoryRepository()

class StockService:

    # test para probar el circuit si anda o no
    #@db_breaker
    #def faulty_method(self):
    #    raise Exception("Simulated database error")

    # TODO: esto despues se puede desacoplar mas pero por ahora tener un stockservice que haga todo esta bien

    #articulos
    @db_breaker
    def add_article(self, article):
        article_repository.create(article)
        return article_schema.dump(article)
    
    @db_breaker
    def get_articles(self):
        return article_repository.find_all()
    
    @db_breaker
    def get_article(self, id):
        return article_repository.find_by_id(id)
    
    @db_breaker
    def edit_article(self, article):
        article_repository.update(article)
        return article_schema.dump(article)
    
    @db_breaker
    def delete_article(self, article):
        article_repository.delete(article)
        return article_schema.dump(article)
    
    @db_breaker
    def soft_delete_article(self, article):
        article_repository.soft_delete(article)
        return article_schema.dump(article)

    #categorias
    @db_breaker
    def add_category(self, category):
        category_repository.create(category)
        return category_schema.dump(category)
    
    @db_breaker
    def get_category(self, id):
        return category_repository.find_by_id(id)
    
    