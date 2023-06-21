from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Length



class SchodyBetonowe(FlaskForm):
    email = StringField('Wpisz swój e-mail', validators=[DataRequired()])
    wood_type = SelectField('Jaki gatunek drewna państwa interesuje', choices=[('Amazakque', 'Amazakque'), 
                                                                               ('Bodo', 'Bodo'), 
                                                                               ('Dąb','Dąb'), 
                                                                               ('Dąb czerwony', 'Dąb czerwony'),
                                                                               ('Doussie','Doussie'),
                                                                               ('Iroko','Iroko'),
                                                                               ('Jesion', 'Jesion'),
                                                                               ('Merbau', 'Merbau'),
                                                                               ('Orzech Amerykański','Orzech Amerykański'),
                                                                               ('Sapeli','Sapeli'),
                                                                               ('Thermojesion','Thermojesion'),
                                                                               ('Tauari (dąb brazilijski)','Tauari (dąb brazilijski)'),
                                                                               ('Wenge','Wenge'),
                                                                               ('Teak','Teak'),
                                                                               ('lub inne napisz jakie','lub inne napisz jakie')
                                                                               ])
    step_count = StringField('Proszę podać ilość stopni', validators=[DataRequired(), Length(max=2)])

    stairs_type = RadioField('Proszę wybrać jeden z poniższych układów schodów', choices=[('proste', 'proste'),
                                                                                          ('z podestem w ksztalcie litery L', 'z podestem w ksztalcie litery L'),
                                                                                          ('z podestem w ksztalcie litery U','z podestem w ksztalcie litery U'),
                                                                                          ('jednozabiegowe w ksztalcie litery L','jednozabiegowe w ksztalcie litery L'),
                                                                                          ('dwuzabiegowe w ksztalcie litery U','dwuzabiegowe w ksztalcie litery U')
                                                                                          ])
    
    stairs_width = StringField('Szerokość schodów (stopni) w cm', validators=[DataRequired(), Length(max=3)])
    
    step_type = RadioField('Rodzaj podstopni', choices=[('drewniane', 'drewniane'),
                                                        ('z płyty karton-gips', 'z płyty karton-gips'),
                                                        ('z mdf lakierowanego', 'z mdf lakierowanego')
                                                        ])

    step_finish = RadioField('Obróbka schodów', choices=[('cokół', 'cokół'),
                                                         ('wanga', 'wanga'),
                                                         ('bez', 'bez')
                                                        ])
    
    balustrade_type = RadioField('Rodzaj balustrady', choices=[('bez', 'bez'),
                                                               ('drewniana', 'drewniana'),
                                                               ('drewno stal nierdzewna',''),
                                                               ('drewno szkło', ''),
                                                               ('cała szklana','cała szklana'),
                                                               ('wypełnienie kute','wypełnienie kute'),
                                                              ])

    balustrade_info = TextAreaField('dodatkowe informacje o balustradzie')

    led_lighting = RadioField('Czy będzie instalowane oświetlenie LED', choices=[('tak', 'tak'),
                                                                                 ('nie', 'nie')
                                                                                ])
    
    color_change = RadioField('Czy będą barwione na inny kolor', choices=[('tak', 'tak'),
                                                                          ('nie', 'nie')
                                                                         ])

    additional_info = TextAreaField('dodatkowe informacje')

    submit = SubmitField('Wyślij')
