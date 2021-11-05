from common.ma import ma
from marshmallow import validate, fields
from models.addToCar import AddToCarModel
from models.schema.user_schema import UserSchema
from models.schema.product_schema import ProductSchema

class AddToCarSchema(ma.SQLAlchemyAutoSchema):
    class Mate:
        model = AddToCarModel
    id = fields.Int()
    quantity = fields.Str(required = True)
    state = fields.Str(required = True, validate=[validate.Length(min=6, max=36)])
    user = fields.Nested(UserSchema)
    product = fields.Nested(ProductSchema)
    insert_time = fields.Str()
    update_time = fields.Str()