from domain import MovieEntry
from flask import jsonify
from globals import Globals

class RecommendationService:

    def execute(self, userid):

        print(Globals.recommendObjs)

        data = [MovieEntry("1", "God Father", "https://m.media-amazon.com/images/M/MV5BMjQxM2YyNjMtZjUxYy00OGYyLTg0MmQtNGE2YzNjYmUyZTY1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", 4),
                MovieEntry("2", "God Father 2", "https://m.media-amazon.com/images/M/MV5BMjQxM2YyNjMtZjUxYy00OGYyLTg0MmQtNGE2YzNjYmUyZTY1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", 5)]
        return jsonify([e.serialize() for e in data])
