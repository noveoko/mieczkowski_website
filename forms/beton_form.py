from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SchodyBetonowe(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    wood_species = SelectField('Gatunek drewna', choices=[
        # Choices
    ], validators=[DataRequired()])
    num_steps = StringField('Ilość stopni', validators=[DataRequired()])
    stair_layout = RadioField('Układ schodów', choices=[
        # Choices
    ], validators=[DataRequired()])
    stairs_width_cm = StringField('Szerokość schodów', validators=[DataRequired()])
    stairs_type = RadioField('Rodzaj podstopni', choices=[
        # Choices
    ], validators=[DataRequired()])
    step_trim = RadioField('Obróbka stopni', choices=[
        # Choices
    ], validators=[DataRequired()])
    balustrade_type = RadioField('Rodzaj balustrady', choices=[
        # Choices
    ], validators=[DataRequired()])
    balustrade_info = TextAreaField('Informacje o balustradzie', validators=[DataRequired()])
    led_lighting = RadioField('Oświetlenie LED', choices=[
        ('tak', 'tak'),
        ('nie', 'nie'),
    ], validators=[DataRequired()])
    will_be_colored = RadioField('Kolor na zamówienie', choices=[
        ('tak', 'tak'),
        ('nie', 'nie'),
    ], validators=[DataRequired()])
    additional_information = TextAreaField('Dodatkowe informacje')
    submit = SubmitField('Wyślij')