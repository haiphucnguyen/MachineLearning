from flask import jsonify
from domain import Person
from globals import Globals

class UserService:

    def execute(self):
        ratings_df = Globals.recommendObjs["ratings_df"]

        limit_users = ratings_df.select('userId').distinct().take(10)

        data = []
        for u in limit_users:
            tmp = Person("User %d" % u[0], u[0])
            print(tmp)
            data.append(tmp)

        return jsonify([e.serialize() for e in data])
