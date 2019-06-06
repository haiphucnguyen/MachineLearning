from flask import Flask
from flask import jsonify
from domain import Person

# the all-important app variable:
app = Flask(__name__)

@app.route("/users")
def hello():
    data = [Person("Hai", "1"), Person("Quy1", "2")]
    resp = jsonify(users=[e.serialize() for e in data])
    resp.status_code = 200

    return resp

@app.route('/recommendations/<userid>')
def makeRecommendations(userid):
    return "Make recommendation for user " + userid

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')