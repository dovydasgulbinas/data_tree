from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/test'
# cross site scripting prevention
app.config['SECRET_KEY'] = 'mommy-i-made-a-super-secret-api-key'
app.config['SECURITY_REGISTERABLE'] = True

# runs app in debug mode, after changes server will be reloaded automatically
app.debug = True
# creating ORM manager instance
db = SQLAlchemy(app)

# import must occur here else code will break, reason being that models code is referencing db object which yet \
# havent been created . POSITION IS IMPORTANT!
from tree_project import models

# we initialize flask security
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)

# we get our views from outer file. POSITION IS IMPORTANT!
import tree_project.views


