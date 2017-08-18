from flask import Blueprint, render_template
from blog.models import Post

blog = Blueprint('blog', __name__)

posts = Post.all()

@blog.route('/')
def blog_index():
    return render_template('blog/index.html', posts=posts)

@blog.route('/post/<string:post_id>')
def post_page(post_id):
    post = Post.get_post_by_id(post_id)
    return render_template('blog/post.html', post=post)