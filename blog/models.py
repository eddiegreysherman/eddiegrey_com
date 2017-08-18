import uuid

class Post(object):
    def __init__(self, title, content, author_id, created, published, modified, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created = created
        self.published = published
        self.modified = modified

    def __repr__(self):
        return "<Post {}>".format(self.title)

    def get_posts(self):
        pass

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


class User(object):
    def __init__(self, username, password, email, fullname, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.username = username
        self.password = password
        self.email = email
        self.fullname = fullname

    def __repr__(self):
        return "<User {}>".format(self.username)

    def json(self):
        return {
            "_id": self._id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "fullname": self.fullname
        }