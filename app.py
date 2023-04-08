"""Blogly application."""
from flask import Flask, redirect, request, render_template
from models import db, Blog_Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)


@app.route("/")
def root():
    """redirect to users"""
    return redirect("/users")


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

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['image_url'] or None

    profile = Blog_Users(first_name=first_name, last_name=last_name, img_url=img_url)

    db.session.add(profile)
    db.session.commit()

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
    user.img_url = request.form['image_url']

    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Handle form submission for deleting an existing user"""

    user = Blog_Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')




