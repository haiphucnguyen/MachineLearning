from domain import MovieEntry
from flask import jsonify
from globals import Globals

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

spark = SparkSession.builder.appName("Recommendation ALS").getOrCreate()

class RecommendationService:

    def execute(self, userid):

        movies_df = Globals.movies_df
        ratings_df = Globals.ratings_df
        predictions = Globals.predictions

        ###### Training and evaluation

        ######## Get latest movies
        watched_movies = ratings_df.filter(ratings_df['userId'] == userid).select("movieId")

        print("Watched movies {}".format(watched_movies.count()))
        print("Total movies {}".format(movies_df.count()))

        sqlContext = SQLContext(spark.sparkContext)
        # watched_movies.registerTempTable('watchedMovies')
        # movies_df.registerTempTable("movies")

        # unwatched_movies = sqlContext.sql(
        #     "SELECT * FROM movies WHERE movies.movieId NOT IN (SELECT movieId FROM watchedMovies)")
        unwatched_movies = movies_df.filter(~movies_df['movieId'].isin(watched_movies.select("movieId").rdd.map(lambda r:r[0]).collect()))
        # unwatched_movies.registerTempTable('unwatchedMovies')
        # predictions.registerTempTable("predictions")

        # unwatched_movies_rating = sqlContext.sql(
        #     "SELECT * FROM unwatchedMovies INNER JOIN predictions ON unwatchedMovies.movieId = predictions.movieId order by predictions.prediction DESC, predictions.rating DESC")

        unwatched_movies_rating = unwatched_movies.join(predictions, on=['movieId'])
        unwatched_movies_rating.sort('prediction', ascending=False)

        ##### Extract recommended movies

        recommendedMovies = unwatched_movies_rating.take(20)
        data = []
        for r in recommendedMovies:
            data.append(MovieEntry(r['movieId'], r['title'], "UrL %s" % r['title'], r['prediction']))


        # END TEST code

        # data = [MovieEntry("1", "God Father", "https://m.media-amazon.com/images/M/MV5BMjQxM2YyNjMtZjUxYy00OGYyLTg0MmQtNGE2YzNjYmUyZTY1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", 4),
        #         MovieEntry("2", "God Father 2", "https://m.media-amazon.com/images/M/MV5BMjQxM2YyNjMtZjUxYy00OGYyLTg0MmQtNGE2YzNjYmUyZTY1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", 5)]
        return jsonify([e.serialize() for e in data])
