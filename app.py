#!/usr/bin/python3
import os
import sys
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient
from json import dumps
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_cors import CORS


load_dotenv()

from controllers.boat_new import BoatNew
from controllers.boat_update import BoatUpdate
from controllers.boat_get import BoatGet
from controllers.boat_get_list import BoatGetList
from controllers.boat_service_new import BoatServiceNew
from controllers.boat_service_get import BoatServiceGet
from controllers.boat_service_update import BoatServiceUpdate
from controllers.boat_service_get_list import BoatServiceGetList
from controllers.boat_service_remove import BoatServiceRemove
from controllers.boat_image_new import BoatImageNew
from controllers.boat_image_get import BoatImageGet
from controllers.boat_image_remove import BoatImageRemove
from controllers.boat_image_get_list import BoatImageGetList
from controllers.boat_image_update import BoatImageUpdate

from controllers.User import User
from controllers.Login import Login
from controllers.token_refresh import TokenRefresh


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET")
app.config['JWT_SECRET_KEY'] = os.getenv("APP_SECRET")

app.mongo = MongoClient(os.getenv("MONGO_URL"))
api = Api(app, prefix="/api/v1")
##
api.add_resource(User, '/user/new')

api.add_resource(BoatNew, '/boat/new')
api.add_resource(BoatUpdate, '/boat/update/<string:boat_id>')
api.add_resource(BoatGet, '/boat/get/<string:boat_id>')
api.add_resource(BoatGetList, '/boat/getList')
api.add_resource(BoatServiceNew, '/boat/service/new/<string:boat_id>')
api.add_resource(BoatServiceGet, '/boat/service/get/<string:service_id>')
api.add_resource(BoatServiceGetList, '/boat/service/get/list/<string:boat_id>')
api.add_resource(BoatServiceRemove,'/boat/service/remove/<string:service_id>')
api.add_resource(BoatServiceUpdate, '/boat/service/update/<string:service_id>')
api.add_resource(BoatImageGet, '/boat/image/get/<string:boat_image_id>')
api.add_resource(BoatImageNew, '/boat/image/new/<string:boat_id>')
api.add_resource(BoatImageRemove, '/boat/image/remove/<string:boat_image_id>')
api.add_resource(BoatImageGetList, '/boat/image/get/list/<string:boat_id>')
api.add_resource(BoatImageUpdate, '/boat/image/update/<string:boat_image_id>')


api.add_resource(Login,'/login')
api.add_resource(TokenRefresh, '/refresh-token' )

#jwt
jwt = JWTManager(app)

#Cors
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"))