from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.Service import ServiceModel
from flask_restful import Resource, reqparse

class BoatServiceGetList(Resource):

    @jwt_required()
    def get(self, boat_id):
        b =  ServiceModel()
        return b.get_services(boat_id)