import os
from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from passlib.hash import sha256_crypt
import gc
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/rob'
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column('id', db.Integer, primary_key=True)
    article = db.Column('name', db.Unicode)
    date = db.Column('date', db.Date)
    body = db.Column('body', db.Text)
    
    
    def __init__(self, article, date, body):
        self.article = article
        self.date = date
        self.body = body


import robsite.views