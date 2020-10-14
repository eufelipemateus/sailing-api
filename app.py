#!/usr/bin/python3
import os
import sys
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient
from json import dumps
from dotenv import load_dotenv

load_dotenv()

from controllers.Boat import Boat
from controllers.User import User


app = Flask(__name__)
app.mongo = MongoClient(os.getenv("MONGO_URL"))
api = Api(app, prefix="/api/v1")

api.add_resource(Boat, '/boat/new')
api.add_resource(User, '/user/new')


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"))