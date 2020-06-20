#! /usr/bin/env python
# coding: utf-8

import requests_mock
import os
import sys
# in order to not raise ValueError: attempted relative
# import beyond top-level package :
sys.path.append(os.path.realpath(''))
from app.ajax_request import clean_user_query, check_if_status


def test_clean_user_query():
    query = "Donne moi l'adresse du Mont SaintMichel"
    clean_query = clean_user_query(query)
    assert clean_query == "donne mont saintmichel"


def test_check_status():
    results = {'results': [], 'status': 'OK'}
    status = results['status']
    check_if_status(results)
    assert status != 'ZERO_RESULTS'