from flask import Flask, redirect, url_for
from flask_gravatar import Gravatar
from .common.database import Database

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "123fornow"

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

@app.before_first_request
def init_db():
    Database.initialize()

from .views.blog import blog
app.register_blueprint(blog, url_prefix='/blog')

from .views.admin import admin
app.register_blueprint(admin, url_prefix='/admin')

@app.route('/')
def index():
    return redirect(url_for('blog.blog_index'))