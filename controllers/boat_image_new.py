from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import current_app, jsonify, request
from flask_restful import Resource, reqparse
from models.Image import ImageModel
from werkzeug.datastructures import FileStorage
from gridfs import GridFS


class BoatImageNew(Resource):

    @jwt_required
    def post(self, boat_id):
        try:
        # Validate form
            parser = reqparse.RequestParser()
            parser.add_argument(
                'name', type=str, required=True)
            parser.add_argument(
                'description', type=str, required=True)
            parser.add_argument(
                'image', type=FileStorage, location='files')
            body = parser.parse_args()
        except ValueError:
            print(f"[Error] {ValueError}")
             # Returns error
            """  return return_error_json(status=400, json= {
                "status": False,
                "error": "F001",
                "message": "Missing some required field."
            })"""


        fs = GridFS( current_app.mongo['db'])
        image_id = fs.put(body['image'], content_type=body['image'].content_type, filename= body['name'])
        
        image_body = {
            "image_id":image_id,
            "name": body['name'],
            "description": body['description'],
            "boat_id": boat_id
        }


        b =  ImageModel()
        b.insert(image_body)
        
        return jsonify({"respond": True})