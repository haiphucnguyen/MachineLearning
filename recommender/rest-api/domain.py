class Person:
    def __init__(self, displayname, userid, hobbies):
        self.displayname = displayname
        self.userid = userid
        self.hobbies = hobbies

    def serialize(self):
        return {
            'display_name': self.displayname,
            'user_id': self.userid,
            'hobbies': self.hobbies
        }


class BaseMovieEntry:
    def __init__(self, movieid, moviename):
        self.movieid = movieid
        self.moviename = moviename

class TrendingMovieEntry(BaseMovieEntry):
    def __init__(self, movieid, moviename, weight):
        BaseMovieEntry.__init__(self, movieid, moviename)
        self.weight = weight

    def serialize(self):
        return {
            'movieid': self.movieid,
            'moviename': self.moviename,
            'weight': self.weight
        }

class MovieEntry(BaseMovieEntry):
    def __init__(self, movieid, moviename, movieimg, pre_rating):
        BaseMovieEntry.__init__(self, movieid, moviename)
        self.movieimg = movieimg
        self.pre_rating = pre_rating

    def serialize(self):
        return {
            'movieid': self.movieid,
            'moviename': self.moviename,
            'movieimg': self.movieimg,
            'pre_rating': self.pre_rating,
        }
