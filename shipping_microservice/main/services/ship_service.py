from main.repositories import SucursalRepository, OrderRepository, ShipRepository
from main.schemas import SucursalSchema, OrderSchema, ShipSchema

sucursal_repository = SucursalRepository()
order_repository = OrderRepository()
ship_repository = ShipRepository()
sucursal_schema = SucursalSchema()
order_schema = OrderSchema()
ship_schema = ShipSchema()


class ShipService:

    def add_sucursal(self, sucursal):
        sucursal_repository.create(sucursal)
        return sucursal_schema.dump(sucursal)
    
    def get_sucursal(self, id):
        return sucursal_repository.find_by_id(id)
    
    def add_ship(self, ship):
        ship_repository.create(ship)
        return ship_schema.dump(ship)
    
    def get_ship(self, id):
        return ship_repository.find_by_id(id)
    
