from flask_restful import Resource
from flask import request
from main.schemas import OrderSchema
from main.services import OrderService

order_schema = OrderSchema()
order_service = OrderService() 

class OrderController(Resource):

    def post(self):
        order = order_schema.load(request.get_json())
        return order_schema.dump(order_service.add_order(order))
    
    def get(self):
        return order_schema.dump(order_service.get_orders(), many=True)
    
class ArticlesController(Resource):

    def get(self):
        return order_service.get_articles()