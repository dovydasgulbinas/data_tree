from flask_security import UserMixin, RoleMixin
from tree_project import db

# define many to many relationhip between tables args: table_name, column, column
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


# sanity check class
class Test(db.Model):
    __tablename__ = 'test_class'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id: "{0}" <name "{1}"'.format(self.id, self.name)


class Role(db.Model, RoleMixin):
    # we override the name of our table
    __tablename__ = 'role'

    # crete table columns
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    # init allows to add values to db upon creating an instance of this class
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # defines how row data will be displayed based on a query
    def __repr__(self):
        return '<name: "{0}" <description: "{1}"'.format(self.name, self.description)


class User(db.Model, UserMixin):
    """Defines table structure for users that will login."""
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    # will not encrypt password in this example
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    # not used in this example, but in reality we should confirm our user
    confirmed_at = db.Column(db.DateTime())
    # this defines M2M relationship between users and their roles, hence one user can have more than one role
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email, password, active):
        self.email = email
        self.password = password
        self.active = active

    def __repr__(self):
        return '<email: "{0}",  <active: "{1}"'.format(self.email, self.active)
