import unittest, sys

sys.path.append('..')
from app import create_app, db
from main.models import ArticleModel, CategoryModel
from main.services.stock_service import StockService

stock_service = StockService()

class StockServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.stock_service = StockService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    
    def test_category(self):
        category = CategoryModel(
            name="Test Category",
            description="Test Description",
            category_code=1234
        )
        stock_service.add_category(category)
        self.assertGreater(category.id, 0)
        category = stock_service.get_category(category.id)
        self.assertIsNotNone(category)

    # def test_article(self):
    #     article = ArticleModel(
    #         # id=1,
    #         name="Test Article",
    #         description="Test Description",
    #         code=1234,
    #         amount=10,
    #         category_id=1
    #     )
    #     stock_service.add_article(article)
    #     self.assertEqual(article.name, "Test Article")

#     # def test_get_stock(self):
#     #     article = ArticleModel(
#     #         id=1,
#     #         name="Test Article",
#     #         price=10,
#     #         stock=10
#     #     )
#     #     db.session.add(article)
#     #     db.session.commit()
#     #     stock = self.stock_service.get_stock(article.id)
#     #     self.assertEqual(stock, 10)

#     # def test_update_stock(self):
#     #     article = ArticleModel(
#     #         id=1,
#     #         name="Test Article",
#     #         price=10,
#     #         stock=10
#     #     )
#     #     db.session.add(article)
#     #     db.session.commit()
#     #     self.stock_service.update_stock(article.id, 5)
#     #     stock = self.stock_service.get_stock(article.id)
#     #     self.assertEqual(stock, 5)

    


