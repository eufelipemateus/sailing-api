#!/usr/bin/python3
import os
import sys
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient
from json import dumps
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()

from controllers.boat_new import BoatNew
from controllers.boat_update import BoatUpdate
from controllers.boat_get import BoatGet
from controllers.boat_get_list import BoatGetList
from controllers.User import User
from controllers.Login import Login


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET")
app.config['JWT_SECRET_KEY'] = os.getenv("APP_SECRET")

app.mongo = MongoClient(os.getenv("MONGO_URL"))
api = Api(app, prefix="/api/v1")
##
api.add_resource(User, '/user/new')

api.add_resource(BoatNew, '/boat/new')
api.add_resource(BoatUpdate, '/boat/update')
api.add_resource(BoatGet, '/boat/get/<string:boat_id>')
api.add_resource(BoatGetList, '/boat/getList')

api.add_resource(Login,'/login')

#jwt
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"))