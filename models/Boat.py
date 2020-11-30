
from flask import current_app
from utils.prepare import prepare
from bson.objectid import ObjectId


class BoatModel():

    def insert(self, boat):
        return current_app.mongo['db']['Boats'].insert_one(boat).inserted_id
        
    def update(self,user_id, boat_id, boat):
        return current_app.mongo['db']['Boats'].update_one({'_id':ObjectId(boat_id), "user_id": user_id }, {"$set": boat })
    
    def get(self, boat_id):
        boat = current_app.mongo['db']['Boats'].find_one({'_id':ObjectId(boat_id)})
        if boat is not None:
            return boat
        else:
            return False

    def get_boats(self):
        return [prepare(n) for n in current_app.mongo['db']['Boats'].find()]