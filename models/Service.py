
from flask import current_app
from utils.prepare import prepare
from bson.objectid import ObjectId

class ServiceModel():

    def insert(self, services):
        current_app.mongo['db']['Services'].insert_one(services)
        return prepare(current_app.mongo['db']['Services'].find_one(services))

    def get(self, service_id):
        return prepare(current_app.mongo['db']['Services'].find_one({'_id':ObjectId(service_id)}))

    def get_services(self, boat_id):
        return [prepare(n) for n in current_app.mongo['db']['Services'].find({'boat_id':boat_id})]

    def remove(self, service_id):
        return current_app.mongo['db']['Services'].delete_one({'_id':ObjectId(service_id)})

    def update(self, service_id, service):
        current_app.mongo['db']['Services'].update_one({'_id':ObjectId(service_id)},  {"$set": service })
        return prepare(current_app.mongo['db']['Services'].find_one({'_id':ObjectId(service_id)}))
