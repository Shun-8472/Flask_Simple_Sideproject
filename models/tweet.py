from sqlalchemy.orm import backref, relationship
from common.db import db
from datetime import datetime

from models.follower import FollowerModel

class TweetModel(db.Model):
    __tablename__ = 'tweet'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(220), unique=True, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.now)
    update_date = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)

    user = relationship("UserModel", foreign_keys=[uid], backref = backref("user", uselist = True))

    def __init__(self, uid, message):
        self.uid = uid
        self.message = message

    def add_tweet(self):
        db.session.add(self)
        db.session.flush()
        db.session.commit()
        return self.id

    def update_tweet(self):
        db.session.commit()

    def delete_tweet(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_tweet_byId(cls, tweet_id):
        return cls.query.filter_by(id=tweet_id)

    @classmethod
    def get_tweet_wall(cls, offset, limit):
        return cls.query.order_by(cls.update_date.desc()).limit(limit).offset(offset)

    # @classmethod
    # def get_person_wall(cls, tweet_id, offset, limit):
    #     return cls.query.select_from(FollowerModel).filter(FollowerModel.uid_1 == tweet_id, FollowerModel.uid_2 == cls.uid | (cls.uid==tweet_id))\
    #                     .order_by(cls.update_date.desc()).limit(limit).offset(offset)

    @classmethod
    def get_person_wall(cls, tweet_id, offset, limit):
        return cls.query.filter_by(uid=tweet_id).order_by(cls.update_date.desc()).limit(limit).offset(offset)
        
    @classmethod
    def get_tweet(cls, tweet_id, page, limit):
        return cls.query.filter_by(uid=tweet_id).paginate(page=page, per_page=limit).items