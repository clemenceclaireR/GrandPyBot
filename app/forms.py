#! /usr/bin/env python3
# coding: utf-8


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DialogForm(FlaskForm):
    """
    Form which will be use in the template for the chat,
    data will be then parsed by python scripts and
    sent to ajax
    """
    user_request = StringField(validators=[DataRequired()])
    submit = SubmitField("Envoyer")
