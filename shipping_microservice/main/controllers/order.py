from flask_restful import Resource
from flask import request
from main.schemas import OrderSchema
#from main.services import ShippingService #Falta hacer el servicio shipping_service

order_schema = OrderSchema()
#shipping_service = ShippingService() #Falta hacer el servicio shipping_service

class OrderController(Resource):

    def post(self):
        order = order_schema.load(request.get_json())
        pass #Falta hacer el servicio shipping_service
        #return order_schema.dump(shipping_service.add_order(order))
    
    def get(self):
        pass #Falta hacer el servicio shipping_service
        #return order_schema.dump(shipping_service.get_orders(), many=True)