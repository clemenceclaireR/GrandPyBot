#! /usr/bin/env python3
# coding: utf-8


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DialogForm(FlaskForm):
    """Minimalist form used in /index page
    """
    user_request = StringField(
        "Dis-moi GrandPy, ...", validators=[DataRequired()]
        )
    submit = SubmitField("Dire")
