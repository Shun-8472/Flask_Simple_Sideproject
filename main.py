from app import create_app
from flask_restful import Api
from resources.user import UserSignIn, UserSignUp, UserUpdate
from resources.product import Product, Products
from resources.addToCar import AddToCar, AddToCars

app = create_app('development')

api = Api(app)

api.add_resource(UserSignIn, "/users/SignIn")
api.add_resource(UserSignUp, "/users/SignUp")
api.add_resource(UserUpdate, "/users/<int:user_Id>")

api.add_resource(Product, "/product/<int:product_Id>")
api.add_resource(Products, "/products")

api.add_resource(AddToCar, "/addToCar/<int:addToCar_Id>")
api.add_resource(AddToCars, "/addToCars")