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

app = Flask(__name__)
app.secret_key = 'flasticket_secret'


@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)