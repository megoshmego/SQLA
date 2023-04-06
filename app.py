"""Blogly application."""

from flask import Flask, redirect, request, render_template
from models import db, connect_db, blog_users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route("/")
def list_users():
    """Lists users and shows form."""

    users = blog_users.query.all()
    return render_template("user.html", users=users)



@app.route("/", methods=["POST"])
def add_user():
    """Add pet user redirect to list."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['image_url'] or None

    [profile] = blog_users(first_name=first_name, last_name=last_name, img_url=img_url)

    db.session.add(profile)
    db.session.commit()

    return redirect("/")

@app.route()
