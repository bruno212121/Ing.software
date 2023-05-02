from flask_restful import Resource
from flask import request
from flask import jsonify
from main.schemas import ShipSchema
from main.services import ShipService
import pybreaker

ship_schema = ShipSchema()
ship_service = ShipService()

class ShipController(Resource):

    def post(self):
        try:
            ship = ship_schema.load(request.get_json())
            return ship_schema.dump(ship_service.add_ship(ship)), 201
        except pybreaker.CircuitBreakerError as e:
            print(f"CircuitBreakerError: {e}")
            #return jsonify({"error": "Circuit breaker is open"}), 500
            #preguntar al profe problema con el jsonify

    def get(self):
        pass
        # try: # test para probar el circuit si anda o no
        #     ship_service.faulty_method()
        # except pybreaker.CircuitBreakerError as e:
        #     print(f"CircuitBreakerError: {e}")

        # return ship_schema.dump(ship_service.get_ships(), many=True)
