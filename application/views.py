from flask import render_template
from application import app

from application.auth.models import User

@app.route("/")
def index():
    # return render_template("index.html")
    return render_template("index.html", needs_items=User.find_users_with_no_items())
