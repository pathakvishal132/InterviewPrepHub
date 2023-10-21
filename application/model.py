from application.database import db
from passlib.hash import sha256_crypt
from flask_login import UserMixin, LoginManager


login_manager = LoginManager()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@login_manager.user_loader
def load_manager(id):
    return Manager.query.get(int(id))


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def is_authenticated(self):
        return True

    def check_password_correction(self, attempted_password):
        return sha256_crypt.verify(attempted_password, self.password)

    def get_id(self):
        return str(self.id)

    def is_manager(self):
        return False


class Manager(db.Model):
    __tablename__ = "managers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def is_manager(self):
        return True

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def check_password_correction(self, attempted_password):
        return sha256_crypt.verify(attempted_password, self.password)

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


class Webdev(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    questions = db.Column(db.String, unique=True, nullable=False)
    ans = db.Column(db.String, unique=True, nullable=False)


class MlAi(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    questions = db.Column(db.String, unique=True, nullable=False)
    ans = db.Column(db.String, unique=True, nullable=False)


class Blockchain(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    questions = db.Column(db.String, unique=True, nullable=False)
    ans = db.Column(db.String, unique=True, nullable=False)


class Android(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    questions = db.Column(db.String, unique=True, nullable=False)
    ans = db.Column(db.String, unique=True, nullable=False)


class Dsa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    questions = db.Column(db.String, unique=True, nullable=False)
    ans = db.Column(db.String, unique=True, nullable=False)


class Mechanical(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    questions = db.Column(db.String, unique=True, nullable=False)
    ans = db.Column(db.String, unique=True, nullable=False)


class Electrical(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    questions = db.Column(db.String, unique=True, nullable=False)
    ans = db.Column(db.String, unique=True, nullable=False)


class Civil(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    questions = db.Column(db.String, unique=True, nullable=False)
    ans = db.Column(db.String, unique=True, nullable=False)
