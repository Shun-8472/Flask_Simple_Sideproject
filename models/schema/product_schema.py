from common.ma import ma
from marshmallow import fields
from models.product import ProductModel

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Mate:
        model = ProductModel
    pid = fields.Int()
    name = fields.Str(required = True)
    price = fields.Int(required = True)
    img = fields.Str(required = True)
    description = fields.Str(required = True)
    state = fields.Str(required = True)
    insert_time = fields.Str()
    update_time = fields.Str()