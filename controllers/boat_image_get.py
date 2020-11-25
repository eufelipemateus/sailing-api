from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request, make_response
from models.Image import ImageModel
from flask_restful import Resource, reqparse
from gridfs import GridFS


class BoatImageGet(Resource):

    @jwt_required
    def get(self, boat_image_id):
        
        i =  ImageModel()
        fs = GridFS( current_app.mongo['db'])

        myfile = fs.get(i.get(boat_image_id)['image_id'])
        
        response = make_response(myfile.read())
        response.headers.set('Content-Type', myfile.content_type)
        response.headers.set(
        'Content-Disposition', 'attachment', filename='%s.jpg' % boat_image_id)
        return response