#! /usr/bin/env python3
# coding: utf-8


from flask import Flask
from conf import Config


app = Flask(__name__)
app.config.from_object(Config)


# in order not to get "ImportError: cannot import name 'app' from 'app'"
from app import routes
