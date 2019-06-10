from flask import Flask
from services.users import UserService
from services.recommendation import RecommendationService
from services.trending import TrendingService
from services.contentbase import ContentBaseService
from globals import Globals

# the all-important app variable:
app = Flask(__name__)

@app.route("/users")
def listUsers():
    return UserService().execute()

@app.route("/trendings")
def getGlobalTrending():
    return TrendingService().getGlobalTrending()

@app.route("/trendings/<genre>")
def getGenreTrending(genre):
    return TrendingService().getGenreTrending(genre)


@app.route('/recommendations/<userid>')
def makeRecommendations(userid):
    return RecommendationService().execute(userid)

@app.route('/recommendations/userid=<userid>&&movieid=<movieid>')
def makeRecommendationsByContent(userid, movieid):
    return ContentBaseService().execute(userid, movieid)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')