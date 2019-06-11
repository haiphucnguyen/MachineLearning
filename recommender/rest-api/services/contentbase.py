from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType as Arr, IntegerType, StringType, DoubleType, FloatType
from pyspark.sql.functions import col, count, mean, udf, regexp_replace, concat, collect_set, when, abs, lit
from pyspark.ml.feature import Tokenizer, StopWordsRemover
from functools import reduce
from scipy.spatial.distance import cosine
import re
from flask import jsonify
from domain import MovieEntry

class ContentBaseService:

    genresList = ["Crime", "Romance", "Thriller", "Adventure", "Drama", "War", "Documentary", "Fantasy", "Mystery", \
                  "Musical", "Animation", "Film-Noir", "(no genres listed)", "IMAX", "Horror", "Western", \
                  "Comedy", "Children", "Action", "Sci-Fi"]

    def setGenresMatrix(self, genres):
        movieGenresMatrix = []
        movieGenresList = genres.split('|')
        for x in ContentBaseService.genresList:
            if (x in movieGenresList):
                movieGenresMatrix.append(1)
            else:
                movieGenresMatrix.append(0)
        return movieGenresMatrix

    def execute(self, movieId):
        spark = SparkSession.builder.appName("Recommendation ALS").config("spark.executor.memory", "3g") \
            .config("spark.driver.cores", "4").getOrCreate()

        # do something to prove it works
        movies_df = spark.read.option("header", "true").csv("data/movies.csv", inferSchema=True)
        links_df = spark.read.option("header", "true").csv("data/links.csv", inferSchema=True).cache()
        movies_df = movies_df.join(links_df, on=['movieId']).cache()
        ratings_df = spark.read.option("header", "true").csv("data/ratings.csv", inferSchema=True).cache()
        tags_df = spark.read.option("header", "true").csv("data/tags.csv", inferSchema=True).cache()

        udf_parse_genres = udf(lambda str: self.setGenresMatrix(str), Arr(IntegerType()))

        movies_df = movies_df.withColumn("genresMatrix", udf_parse_genres(col("genres")))
        ratings_df = ratings_df.groupBy("movieId").agg(mean("rating").alias("mean_rating"), count("rating") \
                                                       .alias("count_rating"))
        movies_df = movies_df.join(ratings_df, on="movieId").select("movieId", "title", "genresMatrix", \
                                                                    "mean_rating", "count_rating")

        def getYear(title):
            result = re.search(r'\(\d{4}\)', title)
            if result:
                found = result.group(0).strip('(').strip(')')
            else:
                found = 0
            return int(found)

        udf_parse_year = udf(lambda str: getYear(str), IntegerType())
        movies_df = movies_df.withColumn("year", udf_parse_year(col("title")))

        movies_df = movies_df.withColumn("title", regexp_replace("title", "\(\d{4}\)", ""))

        # Tokenize text
        tokenizer = Tokenizer(inputCol='tag', outputCol='tags_token')
        df_words_token = tokenizer.transform(tags_df).select('movieId', 'tags_token')

        # Remove stop words
        remover = StopWordsRemover(inputCol='tags_token', outputCol='tags_clean')
        df_words_no_stopw = remover.transform(df_words_token).select("movieId", "tags_clean")

        def fudf(val):
            return reduce(lambda x, y: x + y, val)

        flattenUdf = udf(fudf, Arr(StringType()))

        df_words_no_stopw = df_words_no_stopw.groupBy("movieId").agg(collect_set("tags_clean")).select("movieId", \
                    flattenUdf("collect_set(tags_clean)").alias("tags_clean"))

        movies_df = movies_df.join(df_words_no_stopw, on="movieId", how="left").cache()

        tagsPandaDf = df_words_no_stopw.toPandas()
        tagsDict = {}
        for index, x in tagsPandaDf.iterrows():
            wordlist = x['tags_clean']
            tempMovieId = x['movieId']
            for y in wordlist:
                if tempMovieId in tagsDict:
                    # if y not in tagsDict[movieId]:  # Switched off (we will get a non unique list)
                    tagsDict[tempMovieId].append(y)
                else:
                    tagsDict[tempMovieId] = [y]

        genresSimilarityWeight = 0.8
        tagsSimilarityWeight = 2
        yearDistanceWeight = 0.1
        ratingAvgWeight = 0.2

        def tagsSimilarityFunc(basisMovieID, checkedMovieID):
            dictToCheck = tagsDict
            counter = 0
            if basisMovieID in dictToCheck:
                basisTags = dictToCheck[basisMovieID]
                countAllTags = len(basisTags)
                basisTagsDict = {}
                for x in basisTags:
                    if x in basisTagsDict:
                        basisTagsDict[x] += 1
                    else:
                        basisTagsDict[x] = 1

                for x in basisTagsDict:
                    basisTagsDict[x] = basisTagsDict[x] / countAllTags
            else:
                return 0

            if checkedMovieID in dictToCheck:
                checkedTags = dictToCheck[checkedMovieID]
                checkedTags = set(checkedTags)  # Make the list unique
                checkedTags = list(checkedTags)

            else:
                return 0

            for x in basisTagsDict:
                if x in checkedTags: counter += basisTagsDict[x]
            return counter

        tagsSimilarityUdf = udf(tagsSimilarityFunc, FloatType())


        basisGenres = movies_df.filter(movies_df['movieId'] == movieId).select("genresMatrix").collect()[0][0]
        basisYear = movies_df.filter(movies_df['movieId'] == movieId).select('year').collect()[0][0]
        basisRatingAvg = movies_df.filter(movies_df['movieId'] == movieId).select('mean_rating').collect()[0][0]

        def consineFunc(genresVal):
            return float(cosine(basisGenres, genresVal))

        consineUdf = udf(consineFunc, DoubleType())

        moviesWithSim = movies_df.withColumn("similarity", consineUdf("genresMatrix") * genresSimilarityWeight + \
                                             abs(basisRatingAvg - col("mean_rating")) * ratingAvgWeight + \
                                             abs(basisYear - col("year")) / 100 * yearDistanceWeight + \
                                             tagsSimilarityUdf(lit(movieId), col("movieId")) * tagsSimilarityWeight)

        recommendedMovies = moviesWithSim.sort("similarity", ascending=False).select("movieId", "title", "similarity").take(10)

        data = []
        for r in recommendedMovies:
            data.append(MovieEntry(r['movieId'], r['title'], "UrL %s" % r['title'], r['similarity']))

        return jsonify([e.serialize() for e in data])