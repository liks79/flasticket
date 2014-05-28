# -*- coding: utf-8 -*-
"""
    flasticket
    ~~~~~~~~~~~~~
    comment: Simple Ticket Reservation System

    :copyright: (c) 2014 by liks. ( Jou Sung Shik, liks79 __at__ gmail.com )
    :license: MIT LICENSE 2.0 (http://opensource.org/licenses/MIT).
"""

from flask import Flask, render_template, request, session, Response, redirect, url_for
import datetime
from User import User, db
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = 'flasticket_secret'
db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list')
def reserved():
    users = User.query.all()
    return render_template('list.html', users=users)


@app.route('/add', methods=['POST'])
def add():
    rdate = request.form['rdate']
    order = request.form['order']
    person = request.form['person']
    name = request.form['name']
    email = request.form['email']
    tel = request.form['tel']

    user = User(rdate, order, person, name, email, tel)

    print rdate, order, person, name, email, tel
    db.session.add(user)
    db.session.commit()

    return url_for('list')


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
