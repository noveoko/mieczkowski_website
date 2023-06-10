from flask import Flask, render_template, flash, redirect, url_for
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from forms.samonosne_form import SamonosneStairsForm
from forms.beton_form import BetonStairsForm
from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import os
from werkzeug.security import generate_password_hash, check_password_hash
import click
from flask import Flask
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(128))
    #password_hash = db.Column(db.String(128))  # Changed to password_hash (temp turned off)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password) #self.password is actually password hash

@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user(username, password):
    password_hash = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=password_hash)
    
    # Check if the user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user is None:
        db.session.add(new_user)
        db.session.commit()
        click.echo(f"User {username} has been created successfully.")
    else:
        click.echo(f"User {username} already exists.")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):  # Changed to use check_password
            login_user(user)
            return redirect(url_for('protected'))
        else:
            return 'Invalid username or password'
    else:
        return """
            <form method="post">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Submit">
            </form>
            """

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return f'User {username} created successfully.'

@app.route('/protected')
@login_required
def protected():
    return render_template('admin_panel.html', user=current_user.username)

@app.route('/')
def home():
    site_title = app.config['SITE_TITLE']
    return render_template('index.html', site_title=site_title)

@app.route('/galeria')
def galeria():
    # Define images here or pass it as a parameter to the function
    images = os.listdir(os.path.join(app.static_folder, "images/portfolio/"))
    return render_template('galeria.html', images=images, title='Galeria')

@app.route('/oferta')
def oferta():
    return render_template('oferta.html', title='Oferta')

@app.route('/cennik')
def cennik():
    return render_template('cennik.html', title='Cennik')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html', title='Kontakt')

@app.route('/galeria/schody_na_beton')
def schody_na_beton():
    return render_template('schody_na_beton.html')

@app.route('/galeria/schody_samonosne')
def schody_samonosne():
    return render_template('schody_samonosne.html')

@app.route('/galeria/antresole')
def antresole():
    return render_template('antresole.html')

@app.route('/galeria/balustrady')
def balustrady():
    return render_template('balustrady.html')

@app.route('/galeria/szafy')
def szafy():
    return render_template('szafy.html')

@app.route('/galeria/inne')
def inne():
    return render_template('inne.html')

@app.route('/cennik_samonosne', methods=['GET', 'POST'])
def cennik_samonosne():
    form = SamonosneStairsForm()
    if form.validate_on_submit():
        # Process the form data or send an email
        # Example: 
        email = form.email.data
        wood_species = form.wood_species.data
        rodzaj_schodow = form.rodzaj_schodow.data
        # Process and store other form fields as needed
        
        return render_template('success.html')
    return render_template('form.html', form=form)

@app.route('/cennik_beton', methods=['GET', 'POST'])
def cennik_beton():
    form = BetonStairsForm()
    if form.validate_on_submit():
        flash('Form submitted with email {}'.format(
            form.email.data))
        return redirect(url_for('home'))
    return render_template('cennik_beton.html', title='Staircase Form', form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
