from common.ma import ma
from marshmallow import validate, fields
from models.follower import FollowerModel
from models.schema.user_schema import UserSchema

class FollowerSchema(ma.SQLAlchemyAutoSchema):
    class Mate:
        model = FollowerModel
    id = fields.Int()
    uid_1 = fields.Int()
    uid_2 = fields.Int()
    following = fields.Nested(UserSchema)