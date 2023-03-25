from marshmallow import Schema, fields, post_load, post_dump
from main.models import CategoryModel

class CategorySchema(Schema):
    id = fields.Int(dumpt_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    category_code = fields.Int(required=True)
    soft_delete = fields.Boolean(dump_only=True)

    @post_load
    def make_aticle(self, data, **kwargs):
        return CategoryModel(**data)
    
    SKIP_VALUES = ['soft_delete']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }