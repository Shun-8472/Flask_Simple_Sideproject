from common.db import db
from datetime import datetime

class ProductModel(db.Model):
    __tablename__ = 'product'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    db_product_addToCar = db.relationship("AddToCarModel", backref="product")

    def __init__(self, name, price, img, description, state):
        self.name = name
        self.price = price
        self.img = img
        self.description = description
        self.state = state

    def add_product(self):
        db.session.add(self)
        db.session.commit()

    def update_product(self):
        db.session.commit()

    def delete_product(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_product(cls, product_Id):
        return cls.query.filter_by(pid=product_Id).first()

    @classmethod
    def get_all_products(cls):
        return cls.query.all()