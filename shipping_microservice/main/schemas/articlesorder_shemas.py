from marshmallow import Schema, fields, post_load, post_dump
from main.models import ArticlesOrderModel
from .order_schema import OrderSchema

class ArticlesOrderSchema(Schema): 
    id = fields.Int(dump_only=True) 
    article_id = fields.Int(required=True)
    order_id = fields.Int(required=True)
    ammount_article = fields.Int(required=True)
    soft_delete = fields.Boolean(dump_only=True)
    order = fields.Nested('OrderSchema')

    @post_load
    def make_articlesorder(self, data, **kwargs):
        return ArticlesOrderModel(**data)
    
    SKIP_VALUES = ['soft_delete', 'order_id']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }