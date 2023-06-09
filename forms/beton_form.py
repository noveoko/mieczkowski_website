from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired


class BetonStairsForm(FlaskForm):
    email = StringField('Wpisz swój e-mail', validators=[DataRequired(), Email()])
    wood_species = SelectField('Jaki gatunek drewna państwa interesuje', choices=[
        ('Amazakque', 'Amazakque'),
        ('Bodo', 'Bodo'),
        ('Dąb', 'Dąb'),
        # add other species here
    ], validators=[DataRequired()])
    step_count = StringField('Proszę podać ilość stopni', validators=[DataRequired()])
    staircase_type = RadioField('Proszę wybrać jeden z poniższych układów schodów', choices=[
        ('proste', 'proste'),
        # add other types here
    ], validators=[DataRequired()])
    staircase_width = StringField('Szerokość schodów (stopni) w cm', validators=[DataRequired()])
    riser_type = RadioField('Rodzaj podstopni', choices=[
        ('drewniane', 'drewniane'),
        # add other types here
    ], validators=[DataRequired()])
    # add other fields here...
    additional_info = TextAreaField('dodatkowe informacje')
    submit = SubmitField('Wyślij')