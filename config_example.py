class Config(object):
    # Site Content Custom Values ---------------
    SITE_TITLE = "Firma Mieczkowski"

    # Other Config Info ------------------------
    SECRET_KEY = 'GENERATE_A_RANDOM_SECRET_KEY'  # Replace with your own secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app_data.db'

    # Set True (active) or False (inactive) for every category in your portfolio
    PORTFOLIO_CATEGORIES = [
        {
            "schody": {
                "schody_na_beton": True,
                "samonosne": True
            }
        },
        {
            "pozostale": {
                "antresole": True,
                "balustrady": True,
                "szafy": False,
                "inne": False
            }
        }
    ]
