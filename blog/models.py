class Post(object):
    def __init__(self, title, content, author_id, created, published, modified):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created = created
        self.published = published
        self.modified = modified

    def __repr__(self):
        return "<Post {}>".format(self.title)


class User(object):
    def __init__(self, username, password, email, fullname):
        self.username = username
        self.password = password
        self.email = email
        self.fullname = fullname

    def __repr__(self):
        return "<User {}".format(self.username)

