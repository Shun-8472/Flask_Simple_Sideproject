from flask import request
from flask_restful import Resource, abort
from marshmallow import ValidationError

from common.bcrypt import bcrypt
from common.jwt import create_access_token, create_refresh_token

from models.schema.user_sign_schema import UserSignSchema
from models.schema.user_schema import UserSchema
from models.user import UserModel

user_schema = UserSchema()
user_sign_schema = UserSignSchema()

class UserSignUp(Resource):
    def post(self):
        result = user_sign_schema.load(request.json)

        result['password'] = bcrypt.generate_password_hash(result['password']).decode('utf8')
        user = UserModel(result["name"], result["password"], result["role"])
        user.add_user()

        return {
            'message': 'Create user success',
            'post_data': user_schema.dump(result)
        }, 201

class UserUpdate(Resource):
    def get(self, user_Id):
        user = UserModel.get_user(user_Id)

        if not user:
            return {
                'message': 'User not exist!'
            }, 403
        return user_schema.dump(user)

    def put(self, user_Id):
        result = user_sign_schema.load(request.json)
        try:
            user_sign_schema.load(request.json)
        except ValidationError as err:
            return err.normalized_messages(), 433
        
        user = UserModel.get_user(user_Id)
        if not user:
            return {
                'message': 'User not exist!'
            }, 403

        hash_password = bcrypt.generate_password_hash(result['password']).decode('utf8')
        user.name = result['name']
        user.password = hash_password
        user.role = result['role']

        user.update_user()

        return {
            'message': 'Update user success',
            'post_data': user_schema.dump(result)
        }, 201

class UserSignIn(Resource):
    def post(self):
        try:
            user_sign_schema.load(request.json)
        except ValidationError as err:
            return err.normalized_messages(), 433

        result = user_sign_schema.load(request.json)
        user = UserModel.user_login(result['name'])

        if bcrypt.check_password_hash(user.password, result['password']):
            access_token = create_access_token(identity=user.uid)
            refresh_token = create_refresh_token(user.uid)

            return {
                'message': 'Login success',
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        else: 
            return {
                'message': 'Login Fail',
            }, 400

    # Test JWT an redis here
    # @jwt_required()
    # @cache.cached(timeout=50, key_prefix='users')
    # def get(self):
        # current_user = get_jwt_identity()
        # result = UserModel.get_all_user()
        # if not result:
        #     abort(404, message="Could not find user list")
        # return users_schema.dump(result)