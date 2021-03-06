from common.ma import ma
from marshmallow import validate, fields
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Mate:
        model = UserModel
    uid = fields.Int()
    name = fields.Str(required = True, validate=[validate.Length(min=1, max=30)])
    role = fields.Str()