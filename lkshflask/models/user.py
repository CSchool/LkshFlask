# -*- coding: utf-8 -*-

from flask_bcrypt import generate_password_hash, check_password_hash

from lkshflask import db, login_manager


class User(db.Model):
    """
    User model.
    TODO: Write descriptive docstring
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(64))
    name = db.Column(db.String(32))
    surname = db.Column(db.String(32))
    patronymic = db.Column(db.String(32))
    date_of_birth = db.Column(db.Date)
    privileged = db.Column(db.Boolean)

    def __init__(self, username=username, password=password):
        self.username = username
        self.password = generate_password_hash(password)

    def __str__(self):
        return "<User %r>" % self.username

    @login_manager.user_loader
    @staticmethod
    def load_user(user_id):
        return User.get(user_id)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Yeah, boilerplates

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

