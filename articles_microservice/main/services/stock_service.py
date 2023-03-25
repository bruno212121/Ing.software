from main.schemas import ArticleSchema, CategorySchema
from main.repositories import ArticleRepository, CategoryRepository

article_schema = ArticleSchema()
article_repository = ArticleRepository()
category_schema = CategorySchema()
category_repository = CategoryRepository()

class StockService:

    def add_article(self, article):
        article_repository.create(article)
        return article_schema.dump(article)
    
    def add_category(self, category):
        category_repository.create(category)
        return category_schema.dump(category)