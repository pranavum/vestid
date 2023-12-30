from . import db
from flask_login import UserMixin
from sqlalchemy_file import File, FileField

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    models = db.relationship('Model')

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    content = db.Column(FileField)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))