import unittest, sys

sys.path.append('..')
from app import create_app, db
from main.models import SucursalModel, OrderModel, ShipModel
from main.services.ship_service import ShipService
from main.services.order_service import OrderService

ship_service = ShipService()
order_service = OrderService()

class ShipServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.ship_service = ShipService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
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


    def test_ship(self):
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

        ship = ShipModel(
            id_order=order.id,
            ship_code="1234",
            status="Enviado"
        )
        ship_service.add_ship(ship)
        self.assertGreater(ship.id, 0)
        ship = ship_service.get_ship(ship.id)
        self.assertIsNotNone(ship)

