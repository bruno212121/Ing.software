from flask_restful import Resource
from flask import request
from main.schemas import ShipSchema
from main.services import ShipService

ship_schema = ShipSchema()
#shipping_service = ShippingService() #Falta hacer el  ship_service

class ShipController(Resource):

    def post(self):
        article = ship_schema.load(request.get_json())
        pass
        # Falta hacer ship_service
        #return ship_schema.dump(ship_service.add_ship(ship))
    
    def get(self):
        pass
        # return ship_schema.dump(ship_service.get_ships(), many=True)
