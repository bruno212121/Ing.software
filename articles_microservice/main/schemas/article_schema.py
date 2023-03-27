from marshmallow import Schema, fields, post_load, post_dump
from main.models import ArticleModel
from .category_schema import CategorySchema

class ArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    code = fields.Int(required=True)
    amount = fields.Int(required=True)
    category_id = fields.Int(required=True)
    category = fields.Nested(CategorySchema)
    soft_delete = fields.Boolean(dump_only=True)

    @post_load
    def make_aticle(self, data, **kwargs):
        return ArticleModel(**data)
    
    SKIP_VALUES = ['category_id', 'soft_delete']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }

