from flask import request
from flask_restful import Resource, abort

from models.schema.twitter_schema import TwitterSchema
from models.twitter import TwitterModel

from marshmallow import ValidationError

twitter_schema = TwitterSchema(many=True)
twitters_schema = TwitterSchema(many=True)

class Twitter(Resource):

    def get(self, twitter_Id):
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 20))
        twitter = TwitterModel.get_twitter(twitter_Id, page, limit)
        if not twitter:
            abort(404, message="Twitter not exist!")
        return twitter_schema.dump(twitter)

    def put(self, twitter_Id):
        result = twitter_schema.load(request.json)
        try:
            twitter_schema.load(request.json)
        except ValidationError as err:
            return err, 433
        
        twitter = TwitterModel.get_twitter(twitter_Id)
        if not twitter:
            return {
                'message': 'Twitter not exist!'
            }, 403

        twitter.message = result["message"]
        twitter.update_twitter()

        return {
            'message': 'Update twitter success',
            'twitter_data': twitter_schema.dump(result)
        }, 201

class Twitters(Resource):
    def get(self, user_Id):
        limit = int(request.args.get('limit', 20))
        offset = (int(request.args.get('page', 1)) - 1) * limit
        result = TwitterModel.get_person_wall(user_Id, offset, limit)
        if not result:
            abort(404, message="Could not find twitter list")
        return twitters_schema.dump(result)

    def post(self, user_Id):
        twitter = TwitterModel(user_Id, request.json["message"])

        result = twitters_schema.dump(twitter.get_twitter_byId(twitter.add_twitter()))
        if result:
            return {
                'message': 'Twitte success',
                'twitter_data': result
            }, 201
        else:
            abort(400, message="Twitte Fail!")

class Twitters_wall(Resource):
    def get(self):
        limit = int(request.args.get('limit', 20))
        offset = (int(request.args.get('page', 1)) - 1) * limit
        result = TwitterModel.get_twitter_wall(offset, limit)
        if not result:
            abort(404, message="Could not find twitter list")
        return twitters_schema.dump(result)