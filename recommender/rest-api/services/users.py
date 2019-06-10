from flask import jsonify
from domain import Person
from globals import Globals

class UserService:

    def execute(self):
        ratings_df = Globals.ratings_df

        limit_users = ratings_df.select('userId').distinct().take(10)

        data = []
        for u in limit_users:
            hobbies = ['Action', 'Comedy']
            tmp = Person("User %d" % u[0], u[0], hobbies)
            data.append(tmp)

        return jsonify([e.serialize() for e in data])
