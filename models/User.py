
from flask import current_app

class UserModel():
    def insert(self, user):
        return  current_app.mongo['db']['Users'].insert_one(user)
      