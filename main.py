from app import create_app
from flask_restful import Api
from resources.user import User, Users
from resources.product import Product, Products
from resources.addToCar import AddToCar, AddToCars

app = create_app('development')

api = Api(app)

api.add_resource(User, "/user/<int:user_Id>")
api.add_resource(Users, "/users")

api.add_resource(Product, "/product/<int:product_Id>")
api.add_resource(Products, "/products")

api.add_resource(AddToCar, "/addToCar/<int:addToCar_Id>")
api.add_resource(AddToCars, "/addToCars")