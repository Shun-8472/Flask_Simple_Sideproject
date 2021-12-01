from flask import request
from flask_restful import Resource, abort

from models.schema.follower_schema import FollowerSchema
from models.follower import FollowerModel

following_schema = FollowerSchema(many=True)

class Followers(Resource):

    def post(self, user_Id):

        following = FollowerModel.is_following_exist(user_Id, request.json['following'])

        if following:
            return {
                'message': 'Following already Exist'
            }, 200
        else:
            following = FollowerModel(user_Id, request.json['following'])
            following.add_following()
            return {
                'message': 'Insert Following success'
            }, 201

    def get(self, user_Id):
        result = FollowerModel.get_all_following(user_Id)
        if not result:
            abort(404, message="Could not find following list")
        return following_schema.dump(result)

    def delete(self, user_Id):
        following = FollowerModel.is_following_exist(user_Id, request.json['following'])

        if not following:
            abort(404, message="Could not find following info")
        else:
            following.delete_following()
            return {
                'message': 'Delete Following success'
            }, 201