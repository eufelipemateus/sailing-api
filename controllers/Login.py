from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.User import UserModel
from flask_restful import Resource, reqparse
import bcrypt
import jwt
from dotenv import load_dotenv
import os


load_dotenv()

class Login(Resource):
    def __init__(self):
        self.user = UserModel()

    def post(self):
        try:
            # Validate form
            parser = reqparse.RequestParser()
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

        user = self.user.getByEmail(body['email'])

        if not bcrypt.checkpw(body['password'].encode('utf-8'), user['password']):
            return " 4000"
        else:

            del user['password']
            token = jwt.encode(
                user,
                os.getenv("APP_SECRET")
            )

            return jsonify({'jwt': token, "staus": True})

            