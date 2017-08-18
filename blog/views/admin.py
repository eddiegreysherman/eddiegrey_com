from flask import Blueprint, render_template, request, flash, redirect, url_for
from blog.common.utils import Utils
from blog.models import Post
from blog.models import User

admin = Blueprint('admin', __name__)

@admin.route('/')
def dashboard():
    return render_template('admin/dash.html')

@admin.route('/login')
def login():
    return render_template('admin/login.html')

@admin.route('/new', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # set the author_id by finding the email in session...
        post = Post(title, content, 123456)

        post.create_post()
        flash('New post saved!', category='success')
        return redirect(url_for('.dashboard'))

    return render_template('admin/create_post.html')

@admin.route('/edit', methods=['GET', 'POST'])
def edit_post():
    pass

@admin.route('/user/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = Utils.hash_password(request.form['password'])
        email = request.form['email']
        fullname = request.form['fullname']
        user = User(username, password, email, fullname)

        user.create_user()
        flash('New user saved!', category='success')
        return redirect(url_for('.dashboard'))

    return render_template('admin/create_user.html')

@admin.route('/user/edit', methods=['GET', 'POST'])
def edit_user():
    pass