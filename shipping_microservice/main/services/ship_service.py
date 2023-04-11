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
        ship.ship_code = self.generate_ship_code()
        ship_repository.create(ship)
        return ship_schema.dump(ship)
    
    def get_ship(self, id):
        return ship_repository.find_by_id(id)
    
    def generate_ship_code(self) -> str:
        # genereta ship code with random string and numbers with 10 length
        import random
        import string
        # Se define una cadena con letras y números
        caracteres = string.ascii_letters + string.digits
    
        # Se generan 10 caracteres aleatorios a partir de la cadena definida
        codigo = ''.join(random.choice(caracteres) for i in range(20))

        # convertir a mayusculas
        codigo = codigo.upper()
    
        return codigo
    
