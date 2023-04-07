"""Blogly application."""

from flask import Flask, redirect, request, render_template
from models import db, connect_db, Blog_Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route("/")
def root():
    """redirect to losers"""
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

@app.route('/user/<int:user_id>')
def view_profile(user_id):
    """shows profile"""
    user = Blog_Users.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@app.route('/user/<int:user_id>/edit')
def edit_profile(user_id):
    """edit profile"""
    user = Blog_Users.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id


