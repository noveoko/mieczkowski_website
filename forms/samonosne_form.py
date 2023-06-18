from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length,NumberRange


class SamonosneStairsForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    wood_type = SelectField('Gatunek drewna', choices=[
        ("Amazakque", "Amazakque"),
        ("Bodo", "Bodo"),
        ("Dąb", "Dąb"),
        ("Dąb czerwony", "Dąb czerwony"),
        ("Doussie", "Doussie"),
        ("Iroko", "Iroko"),
        ("Jesion", "Jesion"),
        ("Merbau", "Merbau"),
        ("Orzech Amerykański", "Orzech Amerykański"),
        ("Sapeli", "Sapeli"),
        ("Thermojesion", "Thermojesion"),
        ("Tauari (dąb brazilijski)", "Tauari (dąb brazilijski)"),
        ("Teak", "Teak"),
        ("Wenge", "Wenge"),
        ("lub inne napisz jakie", "lub inne napisz jakie")
    ])
    stairs_type = RadioField('Rodzaj schodow', choices=[
        ("proste", "proste"),
        ("z podestem w ksztalcie litery L", "z podestem w ksztalcie litery L"),
        ("z podestem w ksztalcie litery U", "z podestem w ksztalcie litery U"),
        ("jednozabiegowe w ksztalcie litery L", "jednozabiegowe w ksztalcie litery L"),
        ("dwuzabiegowe w ksztalcie litery U", "dwuzabiegowe w ksztalcie litery U")
    ])
    stairs_with = RadioField('Czy beda to schody z', choices=[
        ("z podstopniami", "z podstopniami"),
        ("bez podstopni", "bez podstopni")
    ])
    balustrade_type = RadioField('Rodzaj balustrady', choices=[
        ("bez", "bez"),
        ("drewniana", "drewniana"),
        ("drewno stal nierdzewna", "drewno stal nierdzewna"),
        ("drewno szklo", "drewno szkło"),
        ("cala szklana", "cała szklana"),
        ("wypelnienie kute", "wypełnienie kute"),
        ("cala balustrada kuta", "cała balustrada kuta")
    ])
    stairs_width_cm = IntegerField('Szerokość schodów (stopni) w cm', validators=[DataRequired(), NumberRange(min=1)])
    floor_height_cm = IntegerField('Wysokość kondygnacji w cm', validators=[DataRequired(), NumberRange(min=1)])
    ceiling_hole_width_cm = IntegerField('Wielkość otworu w suficie (szerokość) w cm', validators=[DataRequired(), NumberRange(min=1)])
    ceiling_hole_length_cm = IntegerField('Wielkość otworu w suficie (długość) w cm', validators=[DataRequired(), NumberRange(min=1)])
    will_be_colored = RadioField('Czy będą barwione na inny kolor', choices=[("tak", "tak"), ("nie", "nie")], validators=[DataRequired()])

    additional_information = TextAreaField('Dodatkowe informacje', validators=[Length(max=500)])
    other_info = TextAreaField('Inne informacje', validators=[Length(max=500)])
    submit = SubmitField('Submit')