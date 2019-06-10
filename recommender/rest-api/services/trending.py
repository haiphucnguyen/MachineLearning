from pyspark.sql.functions import mean, col, count, udf, explode
from pyspark.sql.types import ArrayType, StringType
from globals import Globals
from flask import jsonify
from domain import TrendingMovieEntry

class TrendingService:
    def __init__(self):
        print("Hello")

    def getGlobalTrending(self):
        group_movies = Globals.ratings_df.groupBy("movieId").agg(
            mean("rating").alias("average_rating"), \
            count("rating").alias("count_rating"))
        C = group_movies.agg(mean("average_rating")).collect()[0][0]
        group_movies = group_movies.filter(group_movies["count_rating"] > 10)

        group_movies = group_movies.withColumn("weighted_average", col("count_rating") * col("average_rating") \
                                               / (col("count_rating") + 10) + 10 * C / (col("count_rating") + 10))
        group_movies = group_movies.select("movieId", "weighted_average").orderBy("weighted_average",
                                                                                  ascending=False).limit(10)
        trend_movies = group_movies.join(Globals.movies_df, on="movieId").select("movieId", "title",  "weighted_average")
        trend_movies_list = [list(row) for row in trend_movies.collect()]
        data = []
        for movie in trend_movies_list:
            data.append(TrendingMovieEntry(movie[0], movie[1], movie[2]))

        return jsonify([e.serialize() for e in data])

    def getGenreTrending(self, genre):
        udf_parse_genres = udf(lambda str: str.split("|"), ArrayType(StringType()))
        new_movies_df = Globals.movies_df.select("movieId", "title", udf_parse_genres("genres").alias("genre"))
        new_movies_df = new_movies_df.withColumn("genre", explode("genre"))

        genre_movies_df = new_movies_df.filter(new_movies_df["genre"] == genre).select("movieId", "title")

        genre_ratings_df = Globals.ratings_df.join(genre_movies_df, on="movieId", how="inner")

        genre_group_movies = genre_ratings_df.groupBy("movieId").agg(mean("rating").alias("average_rating"), \
                                                                     count("rating").alias("count_rating"))
        genre_C = genre_group_movies.agg(mean("average_rating")).collect()[0][0]
        genre_group_movies = genre_group_movies.filter(genre_group_movies["count_rating"] > 10)

        genre_group_movies = genre_group_movies.withColumn("weighted_average",
                                                           col("count_rating") * col("average_rating") \
                                                           / (col("count_rating") + 10) + 10 * genre_C / (
                                                                       col("count_rating") + 10))
        genre_group_movies = genre_group_movies.select("movieId", "weighted_average"). \
            orderBy("weighted_average", ascending=False).limit(10)
        genre_trend_movies = genre_group_movies.join(genre_movies_df, on="movieId", how="inner"). \
            select("movieId", "title", "weighted_average")
        genre_trend_movies_list = [list(row) for row in genre_trend_movies.collect()]
        data = []
        for movie in genre_trend_movies_list:
            data.append(TrendingMovieEntry(movie[0], movie[1], movie[2]))

        return jsonify([e.serialize() for e in data])
