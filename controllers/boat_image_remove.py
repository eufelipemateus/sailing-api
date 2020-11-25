from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from flask_restful import Resource, reqparse
from models.Image import ImageModel
from gridfs import GridFS


class BoatImageRemove(Resource):

    @jwt_required
    def delete(self, boat_image_id):

        i =  ImageModel()
        fs = GridFS( current_app.mongo['db'])
        
        image = i.get(boat_image_id)
        image['image_id']

        fs.delete(image['image_id'])
        i.remove(boat_image_id)

        return jsonify({"respond": True})