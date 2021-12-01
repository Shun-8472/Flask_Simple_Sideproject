from flask import request
from flask_restful import Resource, abort

from models.schema.tweet_schema import TweetSchema
from models.tweet import TweetModel

from marshmallow import ValidationError

tweet_schema = TweetSchema(many=True)
tweets_schema = TweetSchema(many=True)

class Tweet(Resource):

    def get(self, tweet_Id):
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 20))
        tweet = TweetModel.get_tweet(tweet_Id, page, limit)
        if not tweet:
            abort(404, message="Tweet not exist!")
        return tweet_schema.dump(tweet)

    def put(self, tweet_Id):
        result = tweet_schema.load(request.json)
        try:
            tweet_schema.load(request.json)
        except ValidationError as err:
            return err, 433
        
        tweet = TweetModel.get_tweet(tweet_Id)
        if not tweet:
            return {
                'message': 'Tweet not exist!'
            }, 403

        tweet.message = result["message"]
        tweet.update_tweet()

        return {
            'message': 'Update tweet success',
            'tweet_data': tweet_schema.dump(result)
        }, 201

class Tweets(Resource):
    def get(self, user_Id):
        limit = int(request.args.get('limit', 20))
        offset = (int(request.args.get('page', 1)) - 1) * limit
        result = TweetModel.get_person_wall(user_Id, offset, limit)
        if not result:
            abort(404, message="Could not find tweet list")
        return tweets_schema.dump(result)

    def post(self, user_Id):
        tweet = TweetModel(user_Id, request.json["message"])

        result = tweets_schema.dump(tweet.get_tweet_byId(tweet.add_tweet()))
        if result:
            return {
                'message': 'Tweet success',
                'tweet_data': result
            }, 201
        else:
            abort(400, message="Tweet Fail!")

class Tweets_wall(Resource):
    def get(self):
        limit = int(request.args.get('limit', 20))
        offset = (int(request.args.get('page', 1)) - 1) * limit
        result = TweetModel.get_tweet_wall(offset, limit)
        if not result:
            abort(404, message="Could not find tweet list")
        return tweets_schema.dump(result)