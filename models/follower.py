from sqlalchemy.orm import relationship
from common.db import db

class FollowerModel(db.Model):
    __tablename__ = 'follower'

    id = db.Column(db.Integer, primary_key=True)
    uid_1 = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
    uid_2 = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)

    following = relationship("UserModel", foreign_keys=[uid_2])

    def __init__(self, uid_1, uid_2):
        self.uid_1 = uid_1
        self.uid_2 = uid_2

    def add_following(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_following(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def is_following_exist(cls, user_id_1, user_id_2):
        return cls.query.filter_by(uid_1=user_id_1, uid_2=user_id_2).first()

    @classmethod
    def get_all_following(cls, user_Id):
        return cls.query.filter_by(uid_1=user_Id).all()