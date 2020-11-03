
from flask import current_app
from utils.prepare import prepare
from bson.objectid import ObjectId


class BoatModel():

    def insert(self, boat):
        return current_app.mongo['db']['Boats'].insert_one(boat)
        
    def update(self, boat_id, boat):
        return current_app.mongo['db']['Boats'].update_one({'_id':ObjectId(boat_id)}, {"$set": boat })
    
    def get(self, boat_id):
        return prepare(current_app.mongo['db']['Boats'].find_one({'_id':ObjectId(boat_id)}))

    def get_boats(self):
        return [prepare(n) for n in current_app.mongo['db']['Boats'].find()]