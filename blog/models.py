import uuid
from blog import Database
import datetime
#from dateutil import tz

#########################
#                       #
#       POST CLASS      #
#                       #
#########################
class Post(object):

    def __init__(self, title, content, author_id, created=None, published=None, modified=None, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created = datetime.datetime.utcnow().strftime('%A %x @ %H:%M') if created is None else created
        self.published = published
        self.modified = modified

    def __repr__(self):
        return "<Post {}>".format(self.title)

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find('posts', {})]

    def create_post(self):
        Database.insert('posts', self.json())

    def update_post(self):
        self.modified = datetime.datetime.utcnow().strftime('%A %x @ %H:%M')
        Database.update('posts', {"_id": self._id}, self.json())

    @classmethod
    def get_post_by_id(cls, post_id):
        return cls(**Database.find_one('posts', {"_id": post_id}))

    def json(self):
        return {
            "_id": self._id,
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "created": self.created,
            "published": self.published,
            "modified": self.modified
        }

#########################
#                       #
#       USER CLASS      #
#                       #
#########################
class User(object):
    def __init__(self, username, password, email, fullname, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.username = username
        self.password = password
        self.email = email
        self.fullname = fullname

    def __repr__(self):
        return "<User {}>".format(self.username)


    def create_user(self):
        Database.insert('users', self.json())

    def json(self):
        return {
            "_id": self._id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "fullname": self.fullname
        }
