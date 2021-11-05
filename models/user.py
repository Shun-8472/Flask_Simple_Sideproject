from common.db import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)

    user_addToCar = db.relationship("AddToCarModel", backref="user", lazy=True)

    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

    def __repr__(self):
        return '<Password %r>' % self.password

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self):
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_user(cls, user_id):
        return cls.query.filter_by(uid=user_id).first()

    @classmethod
    def user_login(cls, user_name):
        return cls.query.filter_by(name=user_name).first()

    # @classmethod
    # def get_all_user(cls):
    #     return cls.query.all()

    def get_all_user(self):
        sql = "select uid, name, role from user"

        return db.engine.execute(sql).fetchall()