from flask import request
from flask_restful import Resource, abort

from models.schema.product_schema import ProductSchema
from models.product import ProductModel

from marshmallow import ValidationError

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class Product(Resource):

    def get(self, product_Id):
        product = ProductModel.get_product(product_Id)
        if not product:
            return {
                'message': 'Product not exist!'
            }, 403
        return product_schema.dump(product)

    def put(self, product_Id):
        result = product_schema.load(request.json)
        try:
            product_schema.load(request.json)
        except ValidationError as err:
            return err, 433
        
        product = ProductModel.get_product(product_Id)
        if not product:
            return {
                'message': 'Product not exist!'
            }, 403

        product.name = result["name"]
        product.price = result["price"]
        product.img = result["img"]
        product.description = result["description"]
        product.state = result["state"]
        
        product.update_product()

        return {
            'message': 'Update user success',
            'post_data': product_schema.dump(result)
        }, 201

class Products(Resource):

    def get(self):
        result = ProductModel.get_all_products()
        if not result:
            abort(404, message="Could not find user list")
        return products_schema.dump(result)

    def post(self):
        result = product_schema.load(request.json)

        product = ProductModel(result["name"], result["price"], result["img"], result["description"], result["state"])
        product.add_product()

        return {
            'message': 'Insert user success',
            'post_data': product_schema.dump(result)
        }, 201