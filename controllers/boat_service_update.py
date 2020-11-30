from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.Service import ServiceModel
from flask_restful import Resource, reqparse

class BoatServiceUpdate(Resource):
    
    @jwt_required
    def post(self, service_id):
        try:
        # Validate form
            parser = reqparse.RequestParser()
            parser.add_argument(
                'service', type=str, required=True)
            parser.add_argument(
                'type', type=str, required=True)
            body = parser.parse_args()
        except ValueError:
            print(f"[Error] {ValueError}")

        b =  ServiceModel()
        return jsonify(b.update(service_id, body))