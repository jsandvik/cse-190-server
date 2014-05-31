from flask import render_template
from . import app

@app.route('/')
def index():
    """
        Index page for logging in.
    """


    return render_template("index.html")