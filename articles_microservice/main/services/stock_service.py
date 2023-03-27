from main.schemas import ArticleSchema, CategorySchema
from main.repositories import ArticleRepository, CategoryRepository

article_schema = ArticleSchema()
article_repository = ArticleRepository()
category_schema = CategorySchema()
category_repository = CategoryRepository()

class StockService:

    # TODO: esto despues se puede desacoplar mas pero por ahora tener un stockservice que haga todo esta bien

    def add_article(self, article):
        article_repository.create(article)
        return article_schema.dump(article)
    
    def get_articles(self):
        return article_repository.find_all()
    
    def add_category(self, category):
        category_repository.create(category)
        return category_schema.dump(category)