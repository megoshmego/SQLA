


First, create a User model for SQLAlchemy. Put this in a models.py file.

It should have the following columns:

  XXX   id, an autoincrementing integer number that is the primary key
    XXX first_name and last_name
    XXX image_url for profile images  - import as binary??




Make good choices about whether things should be required, have defaults, and so on.

Create Flask App


Next, create a skeleton Flask app. You can pattern match from the lecture demo.

It should be able to import the User model, and create the tables using SQLAlchemy. Make sure you have the FlaskDebugToolbar installed — it’s especially helpful when using SQLAlchemy.

Make a Base Template
XX Add a base template with slots for the page title and content. Your other templates should use this.

You can use Bootstrap for this project, but don’t spend a lot of time worrying about styling — this is not a goal of this exercise.

User Interface
Here is what you should build:


USERS PAGE
     has a list of the users , add user button 



New user form 

    "create a user"

    Fist name 

    last name 

    image url 

    "ADD"


USER DETAIL PAGE 

url 

name 

edit 

delet

USER EDIT PAGE 


first name 

last name 

image url 



MAKE ROUTES FOR USERS 

Make routes for the following:

GET /
Redirect to list of users. (We’ll fix this in a later step).

GET /users
Show all users.

Make these links to view the detail page for the user.

Have a link here to the add-user form.

GET /users/new
Show an add form for users

POST /users/new
Process the add form, adding a new user and going back to /users

GET /users/[user-id]
Show information about the given user.
Have a button to get to their edit page, and to delete the user.

GET /users/[user-id]/edit
Show the edit page for a user.

Have a cancel button that returns to the detail page for a user, and a save button that updates the user.

POST /users/[user-id]/edit
Process the edit form, returning the user to the /users page.

POST /users/[user-id]/delete
Delete the user.



BONUS 

Better would be to create a convenience method, get_full_name(), which you could use anywhere you wanted the users’ full name:

XX >>> u = User.query.first()

XXX >>> u.first_name    # SQLAlchemy attribute
'Jane'

XXX >>> u.last_name     # SQLAlchemy attribute
'Smith'

XXX >>> u.get_full_name()
'Jane Smith'



BONUS 

List Users In Order
Make your listing of users order them by last_name, first_name.

You can have SQLAlchemy do this—you don’t need to do it yourself in your route.

Turn Full Name Into a “Property”
Research how to make a Python “property” on a class — this is something that is used like an attribute, but actually is a method. This will let you do things like:

>>> u = User.query.first()

>>> u.first_name    # SQLAlchemy attribute
'Jane'

>>> u.last_name     # SQLAclhemy attribute
'Smith'

>>> u.full_name     # "property"
'Jane Smith'