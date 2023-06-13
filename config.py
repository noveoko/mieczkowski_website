# config.py

class Config(object):
    # Site Content Custom Values ---------------
    SITE_TITLE = "Firma Mieczkowski"

    # Other Config Info ------------------------
    SECRET_KEY = 'dfasdfdsadfsfaff'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app_data.db'

    #Set True (active) or False (inactive) for every category in your portfolio
    PORTFOLIO_CATEGORIES = [{"schody":{
        "schody_na_beton": True,
        "samonosne": True}},
    {"pozostale":{
        "antresole": True,
        "balustrady": True,
        "szafy": False,
        "inne": False}}
    ]