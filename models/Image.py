
from flask import current_app
from utils.prepare import prepare
from bson.objectid import ObjectId

class ImageModel():

    def insert(self, image):
        return current_app.mongo['db']['BoatsImages'].insert_one(image)
        
    def update(self, boat_image_id, image):
        return current_app.mongo['db']['BoatsImages'].update_one({'_id':ObjectId(boat_image_id)}, {"$set": image })
    
    def get(self, boat_image_id):
        return prepare(current_app.mongo['db']['BoatsImages'].find_one({'_id':ObjectId(boat_image_id)}))

    def get_images(self):
        return [prepare(n) for n in current_app.mongo['db']['BoatsImages'].find()]

    def remove(self, boat_image_id):
        return current_app.mongo['db']['BoatsImages'].delete_one({'_id':ObjectId(boat_image_id)})

