from marshmallow import Schema, fields, post_load, post_dump
from main.models import SucursalModel
# from .order_schemas import OrderSchema

class SucursalSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    admin = fields.Boolean()
    # orders = fields.Nested(OrderSchema, many=True)

    @post_load
    def make_sucursal(self, data, **kwargs):
        return SucursalModel(**data)

    @post_dump
    def unmake_sucursal(self, data, **kwargs):
        return data

