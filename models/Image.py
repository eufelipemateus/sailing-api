
from flask import current_app
from utils.prepare import prepareImage
from bson.objectid import ObjectId

class ImageModel():

    def insert(self, image):
        return current_app.mongo['db']['BoatsImages'].insert_one(image).inserted_id
        
    def update(self, boat_image_id, image):
        current_app.mongo['db']['BoatsImages'].update_one({'_id':ObjectId(boat_image_id)}, {"$set": image })
        return prepareImage(current_app.mongo['db']['BoatsImages'].find_one({'_id':ObjectId(boat_image_id)}))
    
    def get(self, boat_image_id):
        return prepareImage(current_app.mongo['db']['BoatsImages'].find_one({'_id':ObjectId(boat_image_id)}))

    def get_images(self, boat_id):
        return current_app.mongo['db']['BoatsImages'].find({'boat_id':ObjectId(boat_id)})

    def remove(self, boat_image_id):
        return current_app.mongo['db']['BoatsImages'].delete_one({'_id':ObjectId(boat_image_id)})

