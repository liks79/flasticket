# -*- coding: utf-8 -*-
"""
    flasticket
    ~~~~~~~~~~~~~
    comment: Simple Ticket Reservation System

    :copyright: (c) 2014 by liks. ( Jou Sung Shik, liks79 __at__ gmail.com )
    :license: MIT LICENSE 2.0 (http://opensource.org/licenses/MIT).
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rdate = db.Column(db.String(10), unique=False)
    order = db.Column(db.String(1), unique=False)
    person = db.Column(db.String(1), unique=False)
    name = db.Column(db.String(100), unique=False)
    email = db.Column(db.String(100), unique=False)
    tel = db.Column(db.String(100), unique=False)

    def __init__(self, rdate, order, person, name, email, tel):
        self.rdate = rdate
        self.order = order
        self.person = person
        self.name = name
        self.email = email
        self.tel = tel

    def __repr__(self):
        return '<User %r>' % self.username
