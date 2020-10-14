
from flask import current_app

class BoatModel():

    def insert(self, boat):
        return current_app.mongo['db']['Boats'].insert_one(boat)
        