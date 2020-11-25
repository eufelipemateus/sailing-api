
from flask import current_app
from utils.prepare import prepare

class UserModel():
    def insert(self, user):
        return  current_app.mongo['db']['Users'].insert_one(user)

    def getByEmail(self, email):
        return prepare(current_app.mongo['db']['Users'].find_one({'email': email}))