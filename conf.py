#! /usr/bin/env python3
# coding: utf-8

from os import environ


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or "dummy-secret-key"


