from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

class Globals:

    def __init__(self):
        print("Init Globals")

    @staticmethod
    def recommendator():
        spark = SparkSession.builder.appName("Recommendation ALS").getOrCreate()

        # do something to prove it works
        movies_df = spark.read.option("header", "true").csv("data/movies.csv", inferSchema=True)
        links_df = spark.read.option("header", "true").csv("data/links.csv", inferSchema=True)
        movies_df = movies_df.join(links_df, on=['movieid'])
        ratings_df = spark.read.option("header", "true").csv("data/ratings.csv", inferSchema=True)
        tags_df = spark.read.option("header", "true").csv("data/tags.csv", inferSchema=True)

        (training, test) = ratings_df.randomSplit([0.8, 0.2])
        # Build the recommendation model using ALS on the training data
        # Note we set cold start strategy to 'drop' to ensure we don't get NaN evaluation metrics
        als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating",
                  coldStartStrategy="drop")
        model = als.fit(training)
        # Evaluate the model by computing the RMSE on the test data
        predictions = model.transform(test)
        predictions.printSchema()
        predictions.orderBy('prediction').show(10)
        evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                        predictionCol="prediction")
        rmse = evaluator.evaluate(predictions)

        Globals.movies_df = movies_df
        Globals.ratings_df = ratings_df
        Globals.tags_df = tags_df
        Globals.predictions = predictions
        Globals.model = model
        Globals.genres = ["Crime", "Romance", "Thriller", "Adventure", "Drama", "War", "Documentary", "Fantasy", "Mystery", \
                  "Musical", "Animation", "Film-Noir", "(no genres listed)", "IMAX", "Horror", "Western", \
                  "Comedy", "Children", "Action", "Sci-Fi"]

Globals.recommendator()