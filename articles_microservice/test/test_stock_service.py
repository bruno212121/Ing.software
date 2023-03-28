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

    def test_article(self):

        category = CategoryModel(
            name="Test Category",
            description="Test Description",
            category_code=1234
        )
        stock_service.add_category(category)
        category = stock_service.get_category(category.id)

        article = ArticleModel(
            name="Test Article",
            description="Test Description",
            code=1234,
            amount=10,
            category_id=category.id
        )
        stock_service.add_article(article)
        self.assertGreater(article.id, 0)
        article = stock_service.get_article(article.id)
        self.assertIsNotNone(article)

    def test_update_article(self):

        category = CategoryModel(
            name="Test Category",
            description="Test Description",
            category_code=1234
        )
        stock_service.add_category(category)
        category = stock_service.get_category(category.id)

        article = ArticleModel(
            name="Test Article",
            description="Test Description",
            code=1234,
            amount=10,
            category_id=category.id
        )
        stock_service.add_article(article)
        self.assertGreater(article.id, 0)
        article = stock_service.get_article(article.id)
        self.assertIsNotNone(article)

        article.amount = 20
        stock_service.edit_article(article)
        article = stock_service.get_article(article.id)
        self.assertEqual(article.amount, 20)

    def test_soft_delete_article(self):

        category = CategoryModel(
            name="Test Category",
            description="Test Description",
            category_code=1234
        )
        stock_service.add_category(category)
        category = stock_service.get_category(category.id)

        article = ArticleModel(
            name="Test Article",
            description="Test Description",
            code=1234,
            amount=10,
            category_id=category.id
        )
        stock_service.add_article(article)
        self.assertGreater(article.id, 0)
        article = stock_service.get_article(article.id)
        self.assertIsNotNone(article)

        stock_service.soft_delete_article(article)
        article = stock_service.get_article(article.id)
        self.assertTrue(article.soft_delete)

    


