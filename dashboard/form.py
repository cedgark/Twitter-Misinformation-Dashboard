from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, validators
from wtforms.validators import ValidationError

class hashtagForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d')
    enddate = DateField('End Date', format='%Y-%m-%d')
    submit_date = SubmitField('Submit')

    def validate_enddate(form, field):
        if field.data < form.startdate.data:
            raise ValidationError("END DATE MUST BE EARLIER THAN START DATE")

class searchBar(FlaskForm):
    searchbar = StringField('Search Bar')
    submit_search = SubmitField('Submit')
