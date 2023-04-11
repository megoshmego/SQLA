"""Blogly application."""
from flask import Flask, redirect, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Blog_Users, connect_db, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)


@app.route("/")
def root():
    """redirect to posts chronologically"""
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return redirect("/users")

@app.errorhandler(404)
def page_not_found(e):
    """show page not found"""
    return render_template('404.html'), 404

@app.route('/users')
def users_index():
    """show a page with info on all users"""

    users = Blog_Users.query.order_by(Blog_Users.last_name, Blog_Users.first_name).all()
    return render_template('users/index.html', users=users)




@app.route('/users/new', methods=["GET"])
def add_user():
    """New User Form"""
    return render_template('users/new.html')


@app.route("/users/new", methods=["POST"])
def new_add_user():
    """Add pet user redirect to list."""

    new_user = Blog_Users(
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()
    flash(f"Blog_User {new_user.full_name} added.")

    return redirect("/users")


@app.route('/users/<int:user_id>')
def show_user(user_id):
    """shows profile"""
    user = Blog_Users.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """edits profile"""
    user = Blog_Users.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user(user_id):
    """Handle form submission for updating an existing user"""

    user = Blog_Users.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()
    flash(f"Blog_Users {user.full_name} edited.")

    return redirect("/users")


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = Blog_Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f"Blog_Users {user.full_name} deleted.")

    return redirect("/users")

@app.route('/users/<int:user_id>/posts/new')
def posts_new_form(user_id):
    """Handle new post"""

    user = Blog_Users.query.get_or_404(user_id)
    return render_template('posts/new.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def posts_new(user_id):
    """Handle new post"""

    user = Blog_Users.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'], content=request.form['content'], user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    flash(f"Post {new_post.title} added.")

    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>')
def posts_show(post_id):
    """Handle new post"""

    post = Post.query.get_or_404(post_id)
    return render_template('posts/show.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def posts_edit_form(post_id):
    """Handle new post"""

    post = Post.query.get_or_404(post_id)
    return render_template('posts/edit.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def posts_edit(post_id):
    """Handle new post"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()
    flash(f"Post {post.title} edited.")

    return redirect(f"/posts/{post_id}")

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def posts_destroy(post_id):
    """Handle new post"""

    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f"Post {post.title} deleted.")

    return redirect("/users/{post.user_id}")



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')




