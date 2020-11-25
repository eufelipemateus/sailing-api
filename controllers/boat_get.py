from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.Boat import BoatModel
from flask_restful import Resource, reqparse

class BoatGet(Resource):

    @jwt_required
    def get(self, boat_id):
        b =  BoatModel()
        return b.get(boat_id)