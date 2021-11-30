from flask import request
from flask_restful import Resource, abort

from models.schema.addToCar_schema import AddToCarSchema
from models.addToCar import AddToCarModel

from marshmallow import ValidationError

addToCar_schema = AddToCarSchema()
addToCars_schema = AddToCarSchema(many=True)

class AddToCar(Resource):

    def get(self, addToCar_Id):
        product = AddToCarModel.get_product(addToCar_Id)
        if not product:
            return {
                'message': 'Product not exist!'
            }, 403
        return addToCar_schema.dump(product)

    def put(self, addToCar_Id):
        result = addToCar_schema.load(request.json)
        try:
            addToCar_schema.load(request.json)
        except ValidationError as err:
            return err, 433
        
        product = AddToCarModel.get_product(addToCar_Id)
        if not product:
            return {
                'message': 'Product not exist!'
            }, 403

        product.update_product()

        return {
            'message': 'Update user success',
            'post_data': addToCar_schema.dump(result)
        }, 201

class AddToCars(Resource):

    def get(self, user_id):
        result = AddToCarModel.get_all_addToCars(user_id)
        if not result:
            abort(404, message="Could not find list")
        return addToCars_schema.dump(result)

    def post(self, user_id):
        request.json["uid"] = int(user_id)
        result = addToCar_schema.load(request.json)

        addToCar = AddToCarModel(result["uid"], result["pid"], result["quantity"], result["state"])
        car = addToCar.is_addToCars_exist(user_id, result["pid"])
        if car:
            return {
                'message': 'Car is exist',
                'data': addToCar_schema.dump(car)
            }, 201

        addToCar.add_addToCar()
        car = addToCar.is_addToCars_exist(user_id, result["pid"])
        return {
            'message': 'Insert cars success',
            'post_data': addToCar_schema.dump(car)
        }, 201