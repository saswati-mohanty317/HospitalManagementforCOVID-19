from wtforms import StringField, IntegerField, SubmitField
from flask_wtf import FlaskForm


class SearchForm(FlaskForm):

    department=StringField('Department Of Doctor ')
    submit = SubmitField('Search Doctor')
