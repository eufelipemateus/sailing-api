from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from models.Service import ServiceModel
from flask_restful import Resource, reqparse

class BoatServiceRemove(Resource):

    @jwt_required
    def delete(self, service_id):
        b =  ServiceModel()
        b.remove(service_id)

        return jsonify({"respond": True}) 