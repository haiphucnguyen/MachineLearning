from domain import MovieEntry
from flask import jsonify
from globals import Globals

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

spark = SparkSession.builder.appName("Recommendation ALS").getOrCreate()

class RecommendationService:

    def execute(self, userId):

        movies_df = Globals.movies_df
        ratings_df = Globals.ratings_df
        model = Globals.model

        users = ratings_df.filter(ratings_df["userId"] == userId).select("userId").distinct()
        userSubsetRecs = model.recommendForUserSubset(users, 10)
        recommendations = userSubsetRecs.select("recommendations").collect()[0][0]

        movieIds = []
        for recommendation in recommendations:
            movieIds.append(recommendation[0])

        recommendedMovies = movies_df.filter(movies_df["movieId"].isin(movieIds)).collect()

        data = []
        for r in recommendedMovies:
            data.append(MovieEntry(r['movieId'], r['title'], "UrL %s" % r['title'], ""))

        return jsonify([e.serialize() for e in data])
