"""This module has required methods for generating whole DB schema that is needed for this project.
This module must be called as a standalone file and should not be imported to  to any other files found in this project.
"""
from tree_project import db
from tree_project import models


def create_tables():
    db.create_all()
    # add some test data to the test_class table
    db.session.add(models.Test('TestField1'))
    # we must commit our changes to db
    db.session.commit()
    # checks if new data was commited to the db
    print(models.Test.query.all())


# will ensure that db tables will be created only if this script is ran as main
if __name__ == '__main__':
    create_tables()
