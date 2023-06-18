from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField
from wtforms.validators import InputRequired, Email

class SchodyBetonowe(FlaskForm):
    email = StringField('Wpisz swój e-mail', validators=[InputRequired(), Email()])
    wood_species = SelectField('Jaki gatunek drewna państwa interesuje', choices=[
        ('Amazakque', 'Amazakque'),
        ('Bodo', 'Bodo'),
        ('Dąb', 'Dąb'),
        ('Dąb czerwony', 'Dąb czerwony'),
        ('Doussie', 'Doussie'),
        ('Iroko', 'Iroko'),
        ('Jesion', 'Jesion'),
        ('Merbau', 'Merbau'),
        ('Orzech Amerykański', 'Orzech Amerykański'),
        ('Sapeli', 'Sapeli'),
        ('Thermojesion', 'Thermojesion'),
        ('Tauari (dąb brazilijski)', 'Tauari (dąb brazilijski)'),
        ('Teak', 'Teak'),
        ('Wenge', 'Wenge'),
        ('lub inne napisz jakie', 'lub inne napisz jakie')
    ], validators=[InputRequired()])
    num_steps = StringField('Proszę podać ilość stopni', validators=[InputRequired()])
    stair_layout = RadioField('Proszę wybrać jeden z poniższych układów schodów', choices=[
        ('proste', 'proste'),
        ('z podestem w ksztalcie litery L', 'z podestem w ksztalcie litery L'),
        ('z podestem w ksztalcie litery U', 'z podestem w ksztalcie litery U'),
        ('jednozabiegowe w ksztalcie litery L', 'jednozabiegowe w ksztalcie litery L'),
        ('dwuzabiegowe w ksztalcie litery U', 'dwuzabiegowe w ksztalcie litery U')
    ], validators=[InputRequired()])
    stair_width = StringField('Szerokość schodów (stopni) w cm', validators=[InputRequired()])
    step_finish = RadioField('Rodzaj podstopni', choices=[
        ('drewniane', 'drewniane'),
        ('z płyty karton-gips', 'z płyty karton-gips'),
        ('z mdf lakierowanego', 'z mdf lakierowanego')
    ], validators=[InputRequired()])
    step_trim = RadioField('Obróbka schodów', choices=[
        ('cokół', 'cokół'),
        ('wanga', 'wanga'),
        ('bez', 'bez obróbki')
    ], validators=[InputRequired()])
    balustrade_type = RadioField('Rodzaj balustrady', choices=[
        ('bez', 'bez'),
        ('drewniana', 'drewniana'),
        ('drewno stal nierdzewna', 'drewno stal nierdzewna'),
        ('drewno szklo', 'drewno szkło'),
        ('cala szklana', 'cała szklana'),
        ('wypelnienie kute', 'wypełnienie kute'),
        ('cala balustrada kuta', 'cała balustrada kuta')
    ], validators=[InputRequired()])
    balustrade_info = TextAreaField('Dodatkowe informacje o balustradzie')
    led_lighting = RadioField('Czy będzie instalowane oświetlenie LED', choices=[
        ('tak', 'tak'),
        ('nie', 'nie')
    ], validators=[InputRequired()])
    custom_color = RadioField('Czy będą barwione na inny kolor', choices=[
        ('tak', 'tak'),
        ('nie', 'nie')
    ], validators=[InputRequired()])
    additional_info = TextAreaField('Dodatkowe informacje')
