from common.ma import ma
from marshmallow import validate, fields
from models.twitter import TwitterModel
from models.schema.user_schema import UserSchema

class TwitterSchema(ma.SQLAlchemyAutoSchema):
    class Mate:
        model = TwitterModel
    id = fields.Int()
    uid = fields.Int(required = True)
    name = fields.Str()
    user = fields.Nested(UserSchema)
    message = fields.Str(required = True, validate=[validate.Length(min=1, max=220)])
    create_date = fields.Str()
    update_date = fields.Str()