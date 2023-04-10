from marshmallow import Schema, fields, post_load, post_dump
from main.models import ShipModel
from .order_schema import OrderSchema

class ShipSchema(Schema):
    id = fields.Int(dump_only=True)
    order = fields.Nested(OrderSchema)
    ship_code = fields.Str(required=True)
    status = fields.Str(required=True)

    @post_load
    def make_ship(self, data, **kwargs):
        return ShipModel(**data)
