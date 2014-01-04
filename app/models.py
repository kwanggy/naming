from datetime import datetime

from flask import *
from flask.ext.sqlalchemy import SQLAlchemy


from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joined_at = db.Column(db.DateTime)
    main_sns = db.Column(db.String)
    twitter_id = db.Column(db.String)
    twitter_token_key = db.Column(db.String)
    twitter_token_secret = db.Column(db.String)
    facebook_id = db.Column(db.String)
    facebook_token_key = db.Column(db.String)
    facebook_token_secret = db.Column(db.String)
    google_id = db.Column(db.String)
    google_token_key = db.Column(db.String)
    google_token_secret = db.Column(db.String)

    def __init__(self, sns, sns_id, token_key, token_secret):
        self.joined_at = datetime.utcnow()
        self.twitter_id = None 
        self.twitter_token_key = None
        self.twitter_token_secret = None
        self.facebook_id = None 
        self.facebook_token_key = None
        self.facebook_token_secret = None
        self.google_id = None 
        self.google_token_key = None
        self.google_token_secret = None

        if sns == 'twitter':
            main_sns = sns
            self.twitter_id = sns_id
            self.twitter_token_key = token_key
            self.twitter_token_secret = token_secret
        elif sns == 'facebook':
            main_sns = sns
            self.facebook_id = sns_id
            self.facebook_token_key = token_key
            self.facebook_token_secret = token_secret
        elif sns == 'google':
            main_sns = sns
            self.google_id = sns_id
            self.google_token_key = token_key
            self.google_token_secret = token_secret

    def picture(self):
        if main_sns == 'twitter':
            return ''
        elif main_sns == 'twitter':
            return 'https://graph.facebook.com/' + self.fbid + '/picture'
        elif main_sns == 'google':
            return ''


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
