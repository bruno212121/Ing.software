import unittest, sys

sys.path.append('..')
from app import create_app, db
from main.models import SucursalModel, OrderModel, ArticlesOrderModel
from main.services.order_service import OrderService
from main.services.ship_service import ShipService

order_service = OrderService()
ship_service = ShipService()

class OrderServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.order_service = OrderService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_order(self):
        sucursal = SucursalModel(
            name="Test Sucursal",
            admin=False
        )
        ship_service.add_sucursal(sucursal)
        sucursal = ship_service.get_sucursal(sucursal.id)

        order = OrderModel(
            order_code="1234",
            sucursal_id=sucursal.id
        )
        order_service.add_order(order)
        self.assertGreater(order.id, 0)
        order = order_service.get_order(order.id)
        self.assertIsNotNone(order)

    def test_articles_order(self):
        sucursal = SucursalModel(
            name="Test Sucursal",
            admin=False
        )
        ship_service.add_sucursal(sucursal)
        sucursal = ship_service.get_sucursal(sucursal.id)

        order = OrderModel(
            order_code="1234",
            sucursal_id=sucursal.id
        )
        order_service.add_order(order)
        self.assertGreater(order.id, 0)
        order = order_service.get_order(order.id)
        self.assertIsNotNone(order)

        article1 = ArticlesOrderModel(
            order_id=order.id,
            article_id=1,
            ammount_article=2
        )
        article2 = ArticlesOrderModel(
            order_id=order.id,
            article_id=2,
            ammount_article=3
        )

        order_service.add_article_order(article1)
        order_service.add_article_order(article2)

        articles = order_service.get_articles_order(order.id)
        self.assertEqual(len(articles), 2)