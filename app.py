import os
import click
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from config import Config
from forms.samonosne_form import SamonosneStairsForm
from forms.beton_form import BetonStairsForm
from utils.products import products as image_links
from collections import defaultdict

app = Flask(__name__)

def filter_valid_images(products):
    for category in products:
        for product in products[category]:
            images = [img for img in product["images"] if os.path.isfile(os.path.join(app.root_path, 'static', img))]
            if len(images) >= 1:
                product["images"] = images
    return products

image_links = filter_valid_images(image_links)

app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user(username, password):
    password_hash = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=password_hash)

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
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('protected'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'


@app.route('/create_user', methods=['POST'])
def create_new_user():
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


import random
import os

import random

import random

import random

import random

@app.route('/galeria')
def galeria():
    PORTFOLIO_CATEGORIES = {
        "schody": {
            "schody_na_beton": True,
            "schody_samonosne": True
        },
        "pozostale": {
            "antresole": True,
            "balustrady": True,
            "szafy": False,
            "inne": False
        }
    }

    # Select only the categories that should be published
    categories_to_publish = {k: [sub_k for sub_k, sub_v in v.items() if sub_v] for k, v in PORTFOLIO_CATEGORIES.items()}

    subcategory_images = {}
    category_used_images = {}

    for category, subcategories in categories_to_publish.items():
        category_images = []  # Initialize with an empty list
        for subcategory in subcategories:
            subcategory_products = image_links.get(subcategory, [])
            if subcategory_products:
                # Exclude images already used for categories
                subcategory_products = [product for product in subcategory_products if product['images'][0] not in category_used_images.values()]
                if subcategory_products:
                    random_product = random.choice(subcategory_products)
                    subcategory_images[subcategory] = random_product['images'][0]  # Assuming every product has at least one image
                    category_images.append(random_product['images'][0])  # Add image to category's list of images

        if category_images:
            category_image = random.choice(category_images)
            category_used_images[category] = category_image  # Save the image used for the category
            category_images.remove(category_image)  # Remove the image from the category's list

    return render_template('galeria.html', title='Galeria', categories=categories_to_publish, category_images=category_used_images, subcategory_images=subcategory_images)


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
        email = form.email.data
        wood_species = form.wood_species.data
        rodzaj_schodow = form.rodzaj_schodow.data
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


@app.route('/portfolio/<category>')
def category(category):
    products = [product for product in image_links[category]]
    photos_in_category = []
    for product in products:
        try:
            product_desc = product['description']
            product_image_links = [link for link in product['images']]  # Remove 'static/' from image paths
            this_product = {'description': product_desc, 'images': product_image_links}
            photos_in_category.append(this_product)
        except Exception as ee:
            print(ee)

    print(f"Single 'image' item: {photos_in_category[0]}")
    return render_template('gallery_view.html', images=photos_in_category)



@app.route('/portfolio/<category>/<product>')
def product(category, product):
    # Assume image_links is a dictionary that maps category names to lists of product dictionaries.
    # Find the correct product based on the provided category and product description.
    for product_dict in image_links[category]:
        if product_dict['description'] == product:
            return render_template('product_view.html', images=product_dict['images'], description=product)
    
    # If the product wasn't found, return a 404 error.
    return "Product not found", 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
