from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.Image import ImageModel
from flask_restful import Resource, reqparse
from utils.return_response import return_error_json, return_json


class BoatImageUpdate(Resource):
    
    @jwt_required
    def post(self, boat_image_id):

        try:
        # Validate form
            parser = reqparse.RequestParser()
            parser.add_argument(
                'name', type=str, required=True)
            parser.add_argument(
                'description', type=str, required=True)
            body = parser.parse_args()
        except ValueError:
            print(f"[Error] {ValueError}")
            # Returns error
            return return_error_json(status=400, json= {
                "status": False,
                "error": "F001",
                "message": "Missing some required field."
            })

        i = ImageModel()
        return i.update(boat_image_id, body)