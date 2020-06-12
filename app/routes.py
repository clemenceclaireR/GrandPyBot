#! /usr/bin/env python3
# coding: utf-8


from flask import render_template
from app import app
from app.forms import DialogForm
from app.ajax_request import ajax_request
from app.api.google_map import GMAP_KEY


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    Initiates the index/main page
    """
    form = DialogForm()
    return render_template('index.html', form=form, key=GMAP_KEY)


@app.route('/ajax', methods=['POST'])
def treat_request():
    """
    Store user request, call the parser on it and get coordinates from
    GoogleMaps. If coords, then call
    MediaWiki API to extract its description.
    """
    return ajax_request()
