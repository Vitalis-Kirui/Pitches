from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch:
    all_pitches = []

    def __init__(self,pitch_title,pitch_category,pitch_itself):
        self.pitch_title = pitch_title
        self.pitch_category =pitch_category
        self.pitch_itself =pitch_itself

    def save_pitch(self):
        Pitch.all_pitches.append(self)        

    @classmethod
    def clear_pitches(cls):
        Pitches.all_pitches.clear()

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pitches = db.relationship("Pitch", backref="user", lazy="dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_category = db.Column(db.String)
    pitch_itself = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, category):
        pitches = Pitch.query.filter_by(pitch_category=category).all()
        return pitches

    @classmethod
    def getPitchId(cls, id):
        pitch = Pitch.query.filter_by(id=id).first()
        return pitch

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()