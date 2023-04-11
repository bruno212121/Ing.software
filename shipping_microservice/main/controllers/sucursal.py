from flask_restful import Resource
from flask import request
from main.schemas import SucursalSchema
from main.services import ShipService

sucursal_schema = SucursalSchema()
ship_service = ShipService()

class SucursalController(Resource):

    def post(self):
        sucursal = sucursal_schema.load(request.get_json())
        return sucursal_schema.dump(ship_service.add_sucursal(sucursal))

    def get(self):
        pass #Falta hacer el servicio shipping_service
        #return order_schema.dump(shipping_service.get_orders(), many=True)