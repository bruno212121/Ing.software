from main.schemas import ArticleSchema, CategorySchema
from main.repositories import ArticleRepository, CategoryRepository

article_schema = ArticleSchema()
article_repository = ArticleRepository()
category_schema = CategorySchema()
category_repository = CategoryRepository()

class StockService:

    # TODO: esto despues se puede desacoplar mas pero por ahora tener un stockservice que haga todo esta bien

    #articulos
    def add_article(self, article):
        article_repository.create(article)
        return article_schema.dump(article)
    
    def get_articles(self):
        return article_repository.find_all()
    
    def get_article(self, id):
        return article_repository.find_by_id(id)
    
    def edit_article(self, article):
        article_repository.update(article)
        return article_schema.dump(article)
    
    def delete_article(self, article):
        article_repository.delete(article)
        return article_schema.dump(article)
    
    def soft_delete_article(self, article):
        article_repository.soft_delete(article)
        return article_schema.dump(article)

    #categorias
    def add_category(self, category):
        category_repository.create(category)
        return category_schema.dump(category)
    
    def get_category(self, id):
        return category_repository.find_by_id(id)
    
    