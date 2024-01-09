#!/usr/bin/env python3
"""This module setup a basic flask app
"""
from flask import flask, render_template



app = Flask(__name__)


@app.route('/')
def home():
    """define the index page of the app
    """
    return render_template("0-index.html") 
