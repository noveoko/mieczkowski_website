from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email



class SamonosneStairsForm(FlaskForm):
    email = StringField('Wpisz swój e-mail', validators=[InputRequired(), Email()])
    wood_species = SelectField('Jaki gatunek drewna państwa interesuje',
                               choices=[('Amazakque', 'Amazakque'), ('Bodo', 'Bodo'), ('Dąb', 'Dąb'),
                                        ('Dąb czerwony', 'Dąb czerwony'), ('Doussie', 'Doussie'),
                                        ('Iroko', 'Iroko'), ('Jesion', 'Jesion'), ('Merbau', 'Merbau'),
                                        ('Orzech Amerykański', 'Orzech Amerykański'), ('Sapeli', 'Sapeli'),
                                        ('Thermojesion', 'Thermojesion'), ('Tauari (dąb brazilijski)', 'Tauari (dąb brazilijski)'),
                                        ('Teak', 'Teak'), ('Wenge', 'Wenge'), ('lub inne napisz jakie', 'lub inne napisz jakie')],
                               validators=[InputRequired()])
    rodzaj_schodow = RadioField('Proszę wybrać jeden z poniższych układów schodów',
                                choices=[('proste', 'proste'),
                                         ('z_podestem_w_ksztalcie_litery_L', 'z podestem w kształcie litery L'),
                                         ('z_podestem_w_ksztalcie_litery_U', 'z podestem w kształcie litery U'),
                                         ('jednozabiegowe_w_ksztalcie_litery_L', 'jednozabiegowe w kształcie litery L'),
                                         ('dwuzabiegowe_w_ksztalcie_litery_U', 'dwuzabiegowe w kształcie litery U')],
                                validators=[InputRequired()])
    czy_bedą_to_schody_z = RadioField('Czy będą to schody z podstopniami',
                                      choices=[('z_podstopniami', 'z podstopniami'), ('bez_podstopni', 'bez podstopni')],
                                      validators=[InputRequired()])
    rodzaj_balustrady = RadioField('Rodzaj balustrady',
                                   choices=[('bez', 'bez'), ('drewniana', 'drewniana'),
                                            ('drewno_stal_nierdzewna', 'drewno stal nierdzewna'),
                                            ('drewno_szklo', 'drewno szkło'), ('cala_szklana', 'cała szklana')],
                                   validators=[InputRequired()])
    wypelnienie_kute = RadioField('Rodzaj balustrady',
                                  choices=[('wypelnienie_kute', 'wypełnienie kute'),
                                           ('cala_balustrada_kuta', 'cała balustrada kuta')],
                                  validators=[InputRequired()])
    dodatkowe_informacje_balustrada = TextAreaField('Dodatkowe informacje o balustradzie')
    szerokosc_stopni = StringField('Szerokość schodów (stopni) w cm', validators=[InputRequired()])
    wysokosc_kondygnacji = StringField('Wysokość kondygnacji w cm', validators=[InputRequired()])
    szerokosc_otworu = StringField('Wielkość otworu w suficie w cm')
    dlugosc_otworu = StringField('')
    czy_beda_barwione_na_inny_kolor = RadioField('Czy będą barwione na inny kolor',
                                                choices=[('tak', 'tak'), ('nie', 'nie')],
                                                validators=[InputRequired()])
    dodatkowe_informacje = TextAreaField('Dodatkowe informacje')
    submit = SubmitField('Wyślij')
