from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.Image import ImageModel
from flask_restful import Resource, reqparse
from utils.prepare import prepareImage
from utils.return_response import return_error_json, return_json


class BoatImageGetList(Resource):

    @jwt_required()
    def get(self, boat_id):
        b =  ImageModel()
        images =b.get_images(boat_id)
        if images:
            return  [prepareImage(n) for n in images ]
        else:
            return return_json({
                "status": False,
                "message": "List images is empty."
            })