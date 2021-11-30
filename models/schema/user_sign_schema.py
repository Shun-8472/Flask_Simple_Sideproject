from common.ma import ma
from marshmallow import validate, fields
from models.user import UserModel

class UserSignSchema(ma.SQLAlchemyAutoSchema):
    class Mate:
        model = UserModel
    uid = fields.Int()
    name = fields.Str(required = True, validate=[validate.Length(min=1, max=30)])
    password = fields.Str(required = True, validate=[validate.Length(min=6, max=36)])
    role = fields.Str()