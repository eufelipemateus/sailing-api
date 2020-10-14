from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.User import UserModel
from flask_restful import Resource, reqparse

class User(Resource):
    # Example http://127.0.0.1:5000/value/<boardid>/<sensorid>/value
    def post(self):

        try:
        # Validate form
            parser = reqparse.RequestParser()
            parser.add_argument(
                'name', type=str, required=True, location='json')
            parser.add_argument(
                'email', type=str, required=True, location='json')
            parser.add_argument(
                'password', type=str, required=True, location='json')
            body = parser.parse_args()
        except ValueError:
            print(f"[Error] {ValueError}")
             # Returns error
            """  return return_error_json(status=400, json= {
                "status": False,
                "error": "F001",
                "message": "Missing some required field."
            })"""



        b =  UserModel()
        b.insert(body)
        
        return jsonify({"respond": True})