from common.db import db
from datetime import datetime

class AddToCarModel(db.Model):
    __tablename__ = 'addtocar'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(5), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column( db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)

    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey('product.pid'), nullable=False)

    def __init__(self, uid, pid, quantity, state):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity
        self.state = state

    def add_addToCar(self):
        db.session.add(self)
        db.session.commit()

    def update_addToCar(self):
        db.session.commit()

    def delete_addToCar(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_addToCar(cls, addToCar_Id):
        return cls.query.filter_by(pid=addToCar_Id).first()

    @classmethod
    def get_all_addToCars(cls, user_Id):
        return cls.query.filter_by(uid=user_Id).all()

    @classmethod
    def is_addToCars_exist(cls, user_Id, product_id):
        return cls.query.filter_by(uid=user_Id, pid=product_id).first()