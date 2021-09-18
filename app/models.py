from . import db

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

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    pass_hash = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    users = db.relationship('User',backref = 'pitch',lazy="dynamic")

    def __repr__(self):
        return f'User {self.title}'