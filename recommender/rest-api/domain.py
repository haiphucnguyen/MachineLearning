class Person:
    def __init__(self, displayname, userid):
        self.displayname = displayname
        self.userid = userid

    def serialize(self):
        return {
            'display_name': self.displayname,
            'user_id': self.userid,
        }


class MovieEntry:
    def __init__(self, movieid, moviename, movieimg, pre_rating):
        self.movieid = movieid
        self.moviename = moviename
        self.movieimg = movieimg
        self.pre_rating = pre_rating

    def serialize(self):
        return {
            'movieid': self.movieid,
            'moviename': self.moviename,
            'movieimg': self.movieimg,
            'pre_rating': self.pre_rating,
        }