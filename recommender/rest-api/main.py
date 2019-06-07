from flask import Flask
from services.users import UserService
from services.recommendation import RecommendationService

# the all-important app variable:
app = Flask(__name__)

@app.route("/users")
def listUsers():
    return UserService().execute()

@app.route('/recommendations/<userid>')
def makeRecommendations(userid):
    return RecommendationService().execute(userid)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')