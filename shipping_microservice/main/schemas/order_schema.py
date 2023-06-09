from marshmallow import Schema, fields, post_load, post_dump
from main.models import OrderModel
from .sucursal_schema import SucursalSchema


class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    order_code = fields.Int(required=True)
    date = fields.Str(required=False)
    sucursal_id = fields.Int(required=True)
    status_out = fields.Boolean(required=False)
    soft_delete = fields.Boolean(dump_only=True)
    sucursal = fields.Nested('SucursalSchema')

    @post_load
    def make_order(self, data, **kwargs):
        return OrderModel(**data)

    SKIP_VALUES = ['soft_delete', 'sucursal_id']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }