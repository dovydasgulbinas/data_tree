from tree_project import app
from tree_project import models


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/labas')
def hi():
    return "super"
