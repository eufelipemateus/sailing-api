from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.Boat import BoatModel
from flask_restful import Resource, reqparse
from utils.prepare import prepare

class BoatGet(Resource):

    @jwt_required()
    def get(self, boat_id):
        b =  BoatModel()
        boat = b.get(boat_id)
        if boat is False :
            return jsonify({"status": False})
        else:
            return jsonify({"status": True, "data": prepare(boat)})