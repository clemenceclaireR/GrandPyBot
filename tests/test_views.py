#! /usr/bin/env python3
# coding: utf-8

from flask import template_rendered
from contextlib import contextmanager
from app import app


@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_index():
    with captured_templates(app) as templates:
        rv = app.test_client().get('/')
        assert rv.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'index.html'


def test_ajax():
    with captured_templates(app):
        rv = app.test_client().get('/ajax')
        assert rv.status_code == 405
