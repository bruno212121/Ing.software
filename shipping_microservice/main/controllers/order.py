from flask_restful import Resource
from flask import request
from main.schemas import OrderSchema
from main.services import ShipService

order_schema = OrderSchema()
ship_service = ShipService() 

class OrderController(Resource):

    def post(self):
        order = order_schema.load(request.get_json())
        return order_schema.dump(ship_service.add_order(order))
    
    def get(self):
        pass #Falta hacer el servicio shipping_service
        #return order_schema.dump(shipping_service.get_orders(), many=True)