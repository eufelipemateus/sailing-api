from flask_jwt_extended import create_access_token
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.User import UserModel
from flask_restful import Resource, reqparse
from utils.return_response import return_error_json, return_json
import bcrypt
import jwt
from dotenv import load_dotenv
import os
import datetime


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
            return return_error_json(status=400, json= {
                "status": False,
                "error": "F001",
                "message": "Missing some required field."
            })

        user = self.user.getByEmail(body['email'])
        
        if user is False:
            return return_error_json(status=400, json= {
                "status": False,
                "error": "F002",
                "message": "Error! in Authentication!!"
            })
        if not bcrypt.checkpw(body['password'].encode('utf-8'), user['password']):
            return return_error_json(status=400, json= {
                "status": False,
                "error": "F002",
                "message": "Error! in Authentication!!"
            })
        else:

            #Don't remove this line is dangerous.
            del user['password']

            jwt_token = create_access_token(identity=user)
            return return_json({'acess_token': jwt_token, "status": True})

            