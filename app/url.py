from flask import Blueprint, render_template, request
from flask_login import login_required, current_user, user_logged_in
from . import db

url = Blueprint('url', __name__)

@url.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return render_template("home.html")
    return render_template("index.html", user=current_user, logged_in=current_user.is_authenticated)