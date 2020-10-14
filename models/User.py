
from flask import current_app

class UserModel():
    def insert(self, user):
        return  current_app.mongo['db']['Users'].insert_one(user)

    def getByEmail(self, email):
        return  current_app.mongo['db']['Users'].find_one({'email': email}, {"_id":  0})