from datetime import datetime

from flask import *
from flask.ext.sqlalchemy import SQLAlchemy


from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joined_at = db.Column(db.DateTime)
    main_sns = db.Column(db.String)

    twitter_user_id = db.Column(db.String)
    twitter_display_name = db.Column(db.String)
    twitter_full_name = db.Column(db.String)
    twitter_profile_url = db.Column(db.String)
    twitter_image_url = db.Column(db.String)
    twitter_token_key = db.Column(db.String)
    twitter_token_secret = db.Column(db.String)

    facebook_user_id = db.Column(db.String)
    facebook_display_name = db.Column(db.String)
    facebook_full_name = db.Column(db.String)
    facebook_profile_url = db.Column(db.String)
    facebook_image_url = db.Column(db.String)
    facebook_token_key = db.Column(db.String)
    facebook_token_secret = db.Column(db.String)

    google_user_id = db.Column(db.String)
    google_display_name = db.Column(db.String)
    google_full_name = db.Column(db.String)
    google_profile_url = db.Column(db.String)
    google_image_url = db.Column(db.String)
    google_token_key = db.Column(db.String)
    google_token_secret = db.Column(db.String)

    def __init__(self, sns_data):
        self.joined_at = datetime.utcnow()
        self.main_sns = db.Column(db.String)

        self.twitter_user_id = None 
        self.twitter_display_name = None
        self.twitter_full_name = None
        self.twitter_profile_url = None
        self.twitter_image_url = None
        self.twitter_token_key = None
        self.twitter_token_secret = None

        self.facebook_user_id = None 
        self.facebook_display_name = None
        self.facebook_full_name = None
        self.facebook_profile_url = None
        self.facebook_image_url = None
        self.facebook_token_key = None
        self.facebook_token_secret = None

        self.google_user_id = None 
        self.google_display_name = None
        self.google_full_name = None
        self.google_profile_url = None
        self.google_image_url = None
        self.google_token_key = None
        self.google_token_secret = None

        sns = sns_data['provider_id']
        main_sns = sns
        if sns == 'twitter':
            self.twitter_user_id = sns_data['provider_user_user_id']
            self.twitter_display_name = sns_data['display_name']
            self.twitter_full_name = sns_data['full_name']
            self.twitter_profile_url = sns_data['profile_url']
            self.twitter_image_url = sns_data['image_url']
            self.twitter_token_key = sns_data['access_token']
            self.twitter_token_secret = sns_data['secret']
        elif sns == 'facebook':
            self.facebook_user_id = sns_data['provider_user_user_id']
            self.facebook_display_name = sns_data['display_name']
            self.facebook_full_name = sns_data['full_name']
            self.facebook_profile_url = sns_data['profile_url']
            self.facebook_image_url = sns_data['image_url']
            self.facebook_token_key = sns_data['access_token']
            self.facebook_token_secret = sns_data['secret']
        elif sns == 'google':
            self.google_user_id = sns_data['provider_user_user_id']
            self.google_display_name = sns_data['display_name']
            self.google_full_name = sns_data['full_name']
            self.google_profile_url = sns_data['profile_url']
            self.google_image_url = sns_data['image_url']
            self.google_token_key = sns_data['access_token']
            self.google_token_secret = sns_data['secret']

    def picture(self):
        if self.main_sns == 'twitter':
            return self.twitter_image_url
        elif self.main_sns == 'facebook':
            return self.facebook_image_url
        elif self.main_sns == 'google':
            return self.google_image_url


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
