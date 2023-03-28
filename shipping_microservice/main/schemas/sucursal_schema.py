from marshmallow import Schema, fields, post_load
from main.models import SucursalModel

class SucursalSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    admin = fields.Boolean(required=True)
    
    @post_load
    def make_ship(self, data, **kwargs):
        return SucursalModel(**data)
