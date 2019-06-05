class Person:
    def __init__(self, displayname, userid):
        self.displayname = displayname
        self.userid = userid

    def serialize(self):
        return {
            'display_name': self.displayname,
            'user_id': self.userid,
        }