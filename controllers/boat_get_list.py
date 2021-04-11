from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.Boat import BoatModel
from flask_restful import Resource, reqparse

class BoatGetList(Resource):

    @jwt_required()
    def get(self):
        b =  BoatModel()
        return b.get_boats()