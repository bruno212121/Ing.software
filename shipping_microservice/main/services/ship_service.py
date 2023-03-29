from main.repositories import SucursalRepository, OrderRepository
from main.schemas import SucursalSchema, OrderSchema

sucursal_repository = SucursalRepository()
order_repository = OrderRepository()
sucursal_schema = SucursalSchema()
order_schema = OrderSchema()

class ShipService:

    def add_sucursal(self, sucursal):
        sucursal_repository.create(sucursal)
        return sucursal_schema.dump(sucursal)
    
    def get_sucursal(self, id):
        return sucursal_repository.find_by_id(id)
    

    def add_order(self, order):
        order_repository.create(order)
        return order_schema.dump(order)
    
    def get_order(self, id):
        return order_repository.find_by_id(id)