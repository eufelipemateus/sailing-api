from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from flask_restful import Resource, reqparse
from models.Service import ServiceModel


class BoatServiceNew(Resource):

    @jwt_required
    def post(self, boat_id):

        try:
        # Validate form
            parser = reqparse.RequestParser()
            parser.add_argument(
                'service', type=str, required=True, location='json')
            parser.add_argument(
                'type', type=str, required=True, location='json')
            body = parser.parse_args()
        except ValueError:
            print(f"[Error] {ValueError}")
             # Returns error
            """  return return_error_json(status=400, json= {
                "status": False,
                "error": "F001",
                "message": "Missing some required field."
            })"""

        s =  ServiceModel()
        return s.insert({'service': body['service'], 'type': body['type'], "boat_id": boat_id})
