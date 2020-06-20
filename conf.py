#! /usr/bin/env python3
# coding: utf-8

from os import environ


class Config(object):
    """
    Get secret key from os or create a dummy one
    """
    SECRET_KEY = environ.get('SECRET_KEY') or "dummy-secret-key"


