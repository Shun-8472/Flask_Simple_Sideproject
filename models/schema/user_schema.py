from common.ma import ma
from marshmallow import validate, fields
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Mate:
        model = UserModel
    uid = fields.Int()
    name = fields.Str(required = True)
    password = fields.Str(required = True, validate=[validate.Length(min=6, max=36)])
    role = fields.Str(required = True)
    # insert_time = fields.DateTime()
    # update_time = fields.DateTime()