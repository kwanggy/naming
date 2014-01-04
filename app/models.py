from datetime import datetime

from flask import *
from flask.ext.sqlalchemy import SQLAlchemy


from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joined_at = db.Column(db.DateTime)
    image_url = db.Column(db.String) 

    twitter_conn_id = db.Column(db.Integer, db.ForeignKey('connection.id'))
    facebook_conn_id = db.Column(db.Integer, db.ForeignKey('connection.id'))
    google_conn_id = db.Column(db.Integer, db.ForeignKey('connection.id'))


    def __init__(self, sns_data):
        self.joined_at = datetime.utcnow()

        self.twitter_conn_id = None
        self.facebook_conn_id = None
        self.google_conn_id = None

        self.twitter_image_url = None
        self.facebook_image_url = None
        self.google_image_url = None

        conn = Connection(sns_data)
        sns = sns_data['provider_id']
        if sns == 'twitter':
            self.twitter_conn_id = conn.id
        elif sns == 'facebook':
            self.facebook_conn_id = conn.id
        elif sns == 'google':
            self.google_conn_id = conn.id
        self.image_url = conn.image_url

    def picture(self):
        if self.main_sns == 'twitter':
            return self.twitter_image_url
        elif self.main_sns == 'facebook':
            return self.facebook_image_url
        elif self.main_sns == 'google':
            return self.google_image_url


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    user_id = db.Column(db.String)
    display_name = db.Column(db.String)
    full_name = db.Column(db.String)
    profile_url = db.Column(db.String)
    image_url = db.Column(db.String)
    token_key = db.Column(db.String)
    token_secret = db.Column(db.String)

    def __init__(self, owner, sns_data):
        self.owner = owner
        self.user_id = sns_data['provider_user_id']
        self.display_name = sns_data['provider_display_name']
        self.full_name = sns_data['provider_full_name']
        self.profile_url = sns_data['provider_profile_url']
        self.image_url = sns_data['provider_image_url']
        self.token_key = sns_data['provider_token_key']
        self.token_secret = sns_data['provider_token_secret']


'''
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.Text)
    lastSubmitted = db.Column(db.DateTime)
    rid= db.Column(db.Integer, db.ForeignKey('room.id'))
    room = db.relationship('Room',
        backref=db.backref('subsmissions', lazy='dynamic'))

    def __init__(self, uid, rid, body):
        self.author = uid
        self.rid = rid
        self.body = body
        self.lastSubmitted = datetime.utcnow()
'''
