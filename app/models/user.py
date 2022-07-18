from flask_login import UserMixin
from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy.orm as orm

user_found = db.Table('user_found', 
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')), 
    db.Column('animal_id', db.Integer, db.ForeignKey('animal.id'))
    )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250))
    animals = db.relationship('Animal', secondary=user_found, backref='finders')

    # animals = orm.relationship() Need to create some sort of way to have a list of objects that sticks with each user

    def hash_my_pass(self, password):
        self.password = generate_password_hash(password)

    def check_my_pass(self, password):
        return check_password_hash(self.password, password)


