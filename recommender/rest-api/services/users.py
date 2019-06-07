from flask import jsonify
from domain import Person

class UserService:

    def execute(self):
        data = [Person("Hai", "1"), Person("Quy1", "2")]
        return jsonify([e.serialize() for e in data])