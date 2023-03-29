import unittest, sys

sys.path.append('..')
from app import create_app, db
from main.models import SucursalModel, OrderModel
from main.services.ship_service import ShipService

ship_service = ShipService()

class ShipServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.ship_service = ShipService()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_sucursal(self):
        sucursal = SucursalModel(
            name="Test Sucursal",
            admin=False
        )
        ship_service.add_sucursal(sucursal)
        self.assertGreater(sucursal.id, 0)
        sucursal = ship_service.get_sucursal(sucursal.id)
        self.assertIsNotNone(sucursal)

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
        ship_service.add_order(order)
        self.assertGreater(order.id, 0)
        order = ship_service.get_order(order.id)
        self.assertIsNotNone(order)
