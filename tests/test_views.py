#! /usr/bin/env python3
# coding: utf-8

from flask import template_rendered
from contextlib import contextmanager
from app import app


@contextmanager
def capture_templates(app):
    """
    Capture template in order to call them in test functions
    """
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_index():
    """
    Tests route for index with its corresponding template
    and success code
    """
    with capture_templates(app) as templates:
        rv = app.test_client().get('/')
        assert rv.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'index.html'


def test_ajax():
    """
    Test a post request with data and get a http success code
    """
    with capture_templates(app):
        tester = app.test_client()
        data = "berlin"
        rv = tester.post('/ajax', headers=[('X-Requested-With',
                                            'XMLHttpRequest')], data=data)
        assert rv.status_code == 200

