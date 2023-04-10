from flask_restful import Resource
from flask import request
from main.schemas import ShipSchema
from main.services import ShipService

ship_schema = ShipSchema()
ship_service = ShipService()

class ShipController(Resource):

    def post(self):
        ship = ship_schema.load(request.get_json())
        return ship_schema.dump(ship_service.add_ship(ship)), 201
    
    def get(self):
        pass
        # return ship_schema.dump(ship_service.get_ships(), many=True)
