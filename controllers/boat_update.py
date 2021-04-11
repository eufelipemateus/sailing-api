from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.Boat import BoatModel
from flask_restful import Resource, reqparse


class BoatUpdate(Resource):
    # Example http://127.0.0.1:5000/value/<boardid>/<sensorid>/value
    @jwt_required()
    def post(self, boat_id):
        try:
        # Validate form
            parser = reqparse.RequestParser()
            parser.add_argument(
                'name', type=str, required=True, location='json')
            parser.add_argument(
                'location', type=str, required=True, location='json')
            parser.add_argument(
                'size', type=str, required=True, location='json')
            parser.add_argument(
                'description', type=str, required=True, location='json')
            parser.add_argument(
                'price', type=str, required=True, location='json')
            body = parser.parse_args()
        except ValueError:
            print(f"[Error] {ValueError}")
             # Returns error
            """  return return_error_json(status=400, json= {
                "status": False,
                "error": "F001",
                "message": "Missing some required field."
            })"""
        current_user = get_jwt_identity()
        
        b =  BoatModel()
        b.update(
            user_id=current_user['id'],
            boat_id=boat_id,
            boat={
                'name':body['name'],
                'location': body['location'],
                'size': body['size'],
                'description': body['description'],
                'price': body['price']
            }
        )

        return jsonify({"respond": True})